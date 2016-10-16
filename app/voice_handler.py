# -*- coding: utf-8 -*-
#from azure_api import xxxx
import re
from user_config import user_config, set_config
from chat_bot_api import chat


"""
处理收到的voice行为 根据特定message可触发不同的自定义action
"""


def handle_voice(message):
    # 根据正则来匹配handler
    for message_pattern, handler in HANDLER_MAP.items():
        if re.match(message, message_pattern):
            return handler(message)
    # 不能匹配特殊行为就用默认处理函数
    return default_handler(message)


def hello_handler(message):
    return "Hello!"


def operation_handler(message):
    # 处理用户特殊指令
    operation = message.lstrip("operation ")
    if operation == "voice":
        print "change voice"
        if user_config["gender"] == "Female":
            set_config("gender", "Male")
        else:
            set_config("gender", "Female")
        return "change voice"
    elif operation == "language":
        print "change language"
        if user_config["lang"] == "en-US":
            set_config("lang", "zh-CN")
        else:
            set_config("lang", "en-US")
        return "change language"
    return "ok"


def default_handler(message):
    return chat(message)


HANDLER_MAP = {
    'hello': hello_handler,
    'operation.*': operation_handler
}
