import requests
import urllib.parse
import os
import time
import uuid


class BaiduService(object):

    def __init__(self, **kwargs):
        self.issue_token_url = 'https://openapi.baidu.com/oauth/2.0/token'
        self.audio2text_url = 'http://vop.baidu.com/server_api'
        self.text2audio_url = 'http://tsn.baidu.com/text2audio'

        self.client_id = kwargs['client_id']
        self.client_secret = kwargs['client_secret']
        self.userid = uuid.uuid1().hex
        self.token = self.gen_token()

    def gen_token(self):
        new_token = self.issue_token()
        return new_token

    def issue_token(self):
        resp = requests.post(
            self.issue_token_url,
            data={
                "grant_type": "client_credentials",
                "client_id": self.client_id,
                "client_secret": self.client_secret
            }
        )
        return resp.json()['access_token']

    def audio2text(self, audio_file, lan='zh'):
        headers = {
            "Content-Type": "audio/wav;rate=8000"
        }
        parms = {
            "cuid": self.userid,
            "token": self.token,
            "lan": lan
        }
        query_string = urllib.parse.urlencode(parms)
        resp = requests.post(
            self.audio2text_url + "?{}".format(query_string),
            headers=headers,
            data=audio_file
        )
        if resp.json()['err_msg'] == 'success.':
            return resp.json()['result'][0].strip(' ，')
        else:
            return 'fail'

    def text2audio(self, text, lan='zh', ctp=1, spd=3, pit=3, vol=9, per=0):
        parms = {
            "tex": text,
            "lan": lan,
            "tok": self.token,
            "ctp": ctp,
            "cuid": self.userid,
            "spd": spd,
            "pit": pit,
            "vol": vol,
            "per": per
        }
        query_string = urllib.parse.urlencode(parms)
        resp = requests.get(
            self.text2audio_url + '?{}'.format(query_string)
        )

        if resp.status_code == 200:
            save_file_name = '{}.mp3'.format(str(time.time())[:10])
            with open('neutron/return_audio/{}'.format(save_file_name), 'wb') as f:
                f.write(resp.content)
            return ('ok', save_file_name)
        else:
            return ('fail', '')
