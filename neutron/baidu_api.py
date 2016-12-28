import requests
import urllib.parse
import os
import time

ISSUE_TOKEN_URL = 'https://openapi.baidu.com/oauth/2.0/token'
CLIENT_ID = os.getenv('BAIDU_VOICE_CLIENT_ID') or 'U0Fzj0kga5prC6wxDMpgNONA'
CLIENT_SECRET = os.getenv('BAIDU_VOICE_CLIENT_SECRET') or 'efeeca301934f987b28c1ae6b9105d8c'
VOICE2TEXT_URL = 'http://vop.baidu.com/server_api'
TEXT2VOICE_URL = 'http://tsn.baidu.com/text2audio'


def gen_token():
    new_token = issue_token()
    return new_token


def issue_token():
    ret = requests.post(
        ISSUE_TOKEN_URL,
        data={
            "grant_type": "client_credentials",
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET
        }
    )
    return ret.json()['access_token']


def recognize(file):
    lan = 'zh'
    headers = {
        "Content-Type": "audio/wav;rate=8000"
    }
    params = {
        "cuid": "tisoga",
        "token": gen_token(),
        "lan": lan,
    }
    query_string = urllib.parse.urlencode(params)
    ret = requests.post(
        VOICE2TEXT_URL + "?{}".format(query_string),
        headers=headers,
        data=file
    )
    if ret.json()['err_msg'] == 'success.':
        return ret.json()['result'][0].strip(' ，')
    else:
        return 'fail'


def synthesize(text):
    parms = {
        "tex": text,
        "lan": "zh",
        "tok": gen_token(),
        "ctp": 1,
        "cuid": "tisoga",
        "spd": 2,
        "pit": 3,
        "vol": 9,
        "per": 0
    }
    query_string = urllib.parse.urlencode(parms)
    resp = requests.get(
        TEXT2VOICE_URL + '?{}'.format(query_string)
    )

    if resp.status_code == 200:
        save_file_name = "voice{}.mp3".format(str(time.time())[:10])
        with open("neutron/return_voice/{}".format(save_file_name), 'wb') as f:
            f.write(resp.content)
        return ('ok', save_file_name)
    else:
        return ('fail', '')
