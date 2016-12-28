import requests
import urllib.parse
import os
import time


def gen_token():
    new_token = issue_token()
    return new_token


def issue_token():
    ret = requests.post(
        'https://openapi.baidu.com/oauth/2.0/token',
        data={
            "grant_type": "client_credentials",
            # "cliend_id": os.getenv('CLIENT_ID'),
            # "client_secret": os.getenv('CLIENT_SECRET')
            "client_id": "U0Fzj0kga5prC6wxDMpgNONA",
            "client_secret": "efeeca301934f987b28c1ae6b9105d8c"
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
        "token": "24.dd515eb1693c0fb9de3d3368229dd651.2592000.1485319770.282335-9124210",
        "lan": lan,
    }
    query_string = urllib.parse.urlencode(params)
    ret = requests.post(
        'http://vop.baidu.com/server_api' + "?{}".format(query_string),
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
        "tok": "24.dd515eb1693c0fb9de3d3368229dd651.2592000.1485319770.282335-9124210",
        "ctp": 1,
        "cuid": "tisoga",
        "spd": 2,
        "pit": 3,
        "vol": 9,
        "per": 0
    }
    query_string = urllib.parse.urlencode(parms)
    resp = requests.get(
        'http://tsn.baidu.com/text2audio' + '?{}'.format(query_string)
    )

    if resp.status_code == 200:
        save_file_name = "voice{}.mp3".format(str(time.time())[:10])
        with open("neutron/return_voice/{}".format(save_file_name), 'wb') as f:
            f.write(resp.content)
        return ('ok', save_file_name)
    else:
        return ('fail', '')
