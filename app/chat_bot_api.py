# -*- coding: utf-8 -*-
import urllib
import requests
import json


CHAT_BOT_URL = "http://api.qingyunke.com/api.php?key=free&appid=0&"


def chat(msg):
    msg_query = urllib.urlencode({'msg': msg})
    ret = requests.get(CHAT_BOT_URL + msg_query)
    ret = json.loads(ret.content)
    return ret['content']


if __name__ == '__main__':
    from IPython import embed
    embed()
