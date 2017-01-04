import urllib
import requests
import json
import uuid


class Turing_AI(object):

    def __init__(self, **kwargs):
        self.url = 'http://www.tuling123.com/openapi/api'
        self.access_key = kwargs['access_key']
        self.userid = uuid.uuid1().hex

    def get_response(self, msg):
        msg_json = {
            "key": self.access_key,
            "info": msg,
            "userid": self.userid
        }
        resp = requests.post(self.url, json=msg_json)
        return resp.json()['text']
