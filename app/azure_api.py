# -*- coding: utf-8 -*-
import requests
import uuid
import urllib
import json


"""
提供与Azure的API交互
"""


ISSUETOKEN_URL = "https://api.cognitive.microsoft.com/sts/v1.0/issueToken"
RECOGNICE_URL = "https://speech.platform.bing.com/recognize"
KEY = "c622adb2893e438796177fadace4a2f2"


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
    headers = {
        "Host": "speech.platform.bing.com",
        "Content-Type": "audio/wav",
        "Authorization": "Bearer %s" % gen_token()
    }
    data = {
        "scenarios": "catsearch",
        "appid": "D4D52672-91D7-4C74-8AD8-42B1D98141A5",
        "locale": "en-US",
        "device.os": "wp7",
        "version": "3.0",
        "format": "json",
        "requestid": "1d4b6030-9099-11e0-91e4-0800200c9a66",
        "instanceid": uuid.uuid4()
    }
    query_string = urllib.urlencode(data)
    ret = requests.post(
        RECOGNICE_URL + "?%s" % query_string,
        headers=headers,
        data=file
        # open("Hack.wav", 'rb')
    )
    ret = json.loads(ret.content)
    if ret['header']['status'] == 'success':
        return ret['results'][0]['name']
    else:
        return "fail to recognize"


if __name__ == '__main__':
    from IPython import embed
    embed()
