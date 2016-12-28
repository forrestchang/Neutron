import urllib
import requests
import json


def turing_robot(msg):
    URL = "http://www.tuling123.com/openapi/api"
    KEY = 'fb583eb0d6a54e758489e971ec2f3aed'
    js = {
        "key": key,
        "info": msg,
        "userid": "tisoga"
    }
    resp = requests.post(URL, json=js)

    return resp.json()['text']
