# -*- coding: utf-8 -*-
import urllib
import requests
import json
from user_config import user_config


CHAT_BOT_URL_MAP = {
    "en-US": {
        "url": "https://aiaas.pandorabots.com/talk/1409613156857/testbot?user_key=b59cb68824a509016ac6dadbbbfa54c4&",
        "key": "input"
    },
    "zh-CN": {
        "url": "http://api.qingyunke.com/api.php?key=free&appid=0&",
        "key": "msg"
    }
}


def chat(msg):
    lang = user_config['lang']
    CHAT_BOT_URL = CHAT_BOT_URL_MAP[lang]['url']
    KEY = CHAT_BOT_URL_MAP[lang]['key']

    msg_query = urllib.urlencode({KEY: msg})
    try:
        if lang == 'en-US':
            ret = requests.post(CHAT_BOT_URL + msg_query)
            return json.loads(ret.content)['responses'][0]
        else:
            ret = requests.get(CHAT_BOT_URL + msg_query)
            return json.loads(ret.content)['content']
    except:
        return ""


if __name__ == '__main__':
    from IPython import embed
    embed()
