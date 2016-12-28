import urllib
import requests
import json


def turing_robot(msg):
    URL = "http://www.tuling123.com/openapi/api"
    js = {
        "key": "fb583eb0d6a54e758489e971ec2f3aed",
        "info": msg,
        "userid": "tisoga"
    }
    resp = requests.post(URL, json=js)
    # if resp.json()['code'] == 10000:
    #     return resp.json()['text']
    # return '你在说什么鬼'
    return resp.json()['text']
