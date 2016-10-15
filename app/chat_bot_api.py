# -*- coding: utf-8 -*-
import urllib
import requests
import json


CHAT_BOT_URL = "https://aiaas.pandorabots.com/talk/1409613156857/testbot?user_key=b59cb68824a509016ac6dadbbbfa54c4&"


def chat(msg):
    msg_query = urllib.urlencode({'input': msg})
    ret = requests.get(CHAT_BOT_URL + msg_query)
    ret = json.loads(ret.content)
    try:
        return ret['responses'][0]
    except:
        return ""


if __name__ == '__main__':
    from IPython import embed
    embed()
