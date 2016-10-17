# -*- coding: utf-8 -*-
#from azure_api import xxxx
import re
from user_config import user_config, set_config
from chat_bot_api import chat


"""
处理收到的voice行为
可根据特定message可触发不同的自定义action
如没有特殊的处理 将调用进入基本的处理流程(聊天)
"""

OPERATION_MAP = {
    "en-US": {
        "operation_prefix": "change ",
        "voice": "voice",
        "language": "language"
    },
    "zh-CN": {
        "operation_prefix": u"切换",
        "voice": u"声音",
        "language": u"语言"
    }
}


def handle_voice(message):
    # 根据正则来匹配handler
    # message = message.encode('utf8')
    for message_pattern, handler in HANDLER_MAP.items():
        if re.match(message_pattern, message):
            return handler(message)
    # 不能匹配特殊行为就用默认处理函数
    return default_handler(message)


def hello_handler(message):
    return "Hello!"


def operation_handler(message):
    # 处理用户特殊指令
    lang = user_config["lang"]
    operation_prefix = OPERATION_MAP[lang]["operation_prefix"]
    voice_opt = OPERATION_MAP[lang]["voice"]
    lang_opt = OPERATION_MAP[lang]["language"]
    operation = message.lstrip(operation_prefix)
    if operation == voice_opt:
        if user_config["gender"] == "Female":
            set_config("gender", "Male")
        else:
            set_config("gender", "Female")
        return "change voice"
    elif operation == lang_opt:
        if lang == "en-US":
            set_config("lang", "zh-CN")
        else:
            set_config("lang", "en-US")
        return "change language"
    return "ok"


def default_handler(message):
    return chat(message)


HANDLER_MAP = {
    'hello': hello_handler,
    'change.*': operation_handler,
     u'切换.*': operation_handler,
}
