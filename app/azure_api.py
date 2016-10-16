# -*- coding: utf-8 -*-
import requests
import uuid
import urllib
import json
import time
from user_config import user_config, set_config


"""
提供与Azure的API交互
"""


ISSUETOKEN_URL = "https://api.cognitive.microsoft.com/sts/v1.0/issueToken"
RECOGNICE_URL = "https://speech.platform.bing.com/recognize"
SYNTHESIZE_URL = "https://speech.platform.bing.com/synthesize"
EMOTION_RECOGNICE_URL = "https://api.projectoxford.ai/emotion/v1.0/recognize"
KEY = "c622adb2893e438796177fadace4a2f2"
EMOTION_KEY = "193bb83ccb144d8ca812b2d5359aaf52"
X_SEARCH_APPID = "e2d7d03b4855434eb05095688ec4bc65"
IMAGE_URL_BASE = "http://121.201.24.49:5000/image/"
SERVICE_NAME_MAP = {
    "en-US": {
        "Female": "Microsoft Server Speech Text to Speech Voice (en-US, ZiraRUS)",
        "Male": "Microsoft Server Speech Text to Speech Voice (en-US, BenjaminRUS)",
    },
    "zh-CN": {
        "Female": "Microsoft Server Speech Text to Speech Voice (zh-CN, Yaoyao, Apollo)",
        "Male": "Microsoft Server Speech Text to Speech Voice (zh-CN, Kangkang, Apollo)",
    }
}


def gen_token():
    """
    使用key去交换一个token 这里每次生成 可用缓存
    """
    new_token = issue_token()
    return new_token


def issue_token():
    ret = requests.post(
        ISSUETOKEN_URL,
        headers={
            "Ocp-Apim-Subscription-Key": KEY
        }
    )
    return ret.content


def recognize(file):
    """
    传入音频file obj 返回text
    """
    lang = user_config['lang']
    headers = {
        "Host": "speech.platform.bing.com",
        "Content-Type": "audio/wav; samplerate=8000; sourcerate=8000; trustsourcerate=true",
        "Authorization": "Bearer %s" % gen_token()
    }
    data = {
        "scenarios": "ulm",
        "appid": "D4D52672-91D7-4C74-8AD8-42B1D98141A5",
        "locale": lang,
        "device.os": "wp7",
        "version": "3.0",
        "format": "json",
        "requestid": "1d4b6030-9099-11e0-91e4-0899200c9a99",
        "instanceid": uuid.uuid4()
    }
    query_string = urllib.urlencode(data)
    ret = requests.post(
        RECOGNICE_URL + "?%s" % query_string,
        headers=headers,
        data=file
        # open("Hack.wav", 'rb')
    )
    try:
        ret = json.loads(ret.content)
    except:
        return "please try a again"

    if ret['header']['status'] == 'success':
        return ret['results'][0]['name']
    else:
        return "fail to recognize"


def synthesize(text):
    """
    传入text 返回保存的音频文件名
    """
    headers = {
        "Host": "speech.platform.bing.com",
        "Content-Type": "application/ssml+xml",
        "Authorization": "Bearer %s" % gen_token(),
        "X-Microsoft-OutputFormat": "riff-8khz-8bit-mono-mulaw",
        "X-Search-Appid": X_SEARCH_APPID,
        "X-Search-ClientID": str(uuid.uuid4()).replace("-", ""),
    }
    gender = user_config.get('gender')
    lang = user_config.get('lang')
    print 'use gender: %s' % gender
    print 'use lang: %s' % lang
    # set_config('gender', 'Male')
    service_name = SERVICE_NAME_MAP[lang][gender]
    body = u"<speak version='1.0' xml:lang='%s'><voice xml:lang='%s' xml:gender='%s' name='%s'>%s</voice></speak>" % (lang.lower(), lang, gender, service_name, text)
    body = body.encode('utf-8')
    print body
    ret = requests.post(
        url=SYNTHESIZE_URL,
        headers=headers,
        data=body
    )
    if ret.status_code == 200:
        save_file_name = "voice%s.wav" % str(time.time())[:10]
        with open("app/return_voice/%s" % save_file_name, "wb") as f:
            f.write(ret.content)
        return "ok", save_file_name
    else:
        return "fail", ""


def emotion_recognize(image_file):
    """
    获取图片情绪
    """
    file_name, postfix = image_file.filename.split(".", 1)
    image_file_name = "%s%s.%s" % (file_name, str(time.time())[:10], postfix)
    image_file_path = "app/image/%s" % image_file_name
    image_file.save(image_file_path)
    ret = requests.post(
        url=EMOTION_RECOGNICE_URL,
        json={
            'url': IMAGE_URL_BASE + image_file_name
        },
        headers={
            "Host": "api.projectoxford.ai",
            "Ocp-Apim-Subscription-Key": EMOTION_KEY
        }
    )
    content = json.loads(ret.content)
    content = content[0]
    res = ""
    try:
        sort_dict = sorted(
            content[u'scores'].iteritems(),
            key=lambda d: d[1],
            reverse=True
        )
        res =  sort_dict[0][0]
    except:
	res  =  "neutral"
    print "aaaaaaaaaaaa res: ", res
    return res


if __name__ == '__main__':
    from IPython import embed
    embed()
