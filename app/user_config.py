# -*- coding: utf-8 -*-


"""
用于保存用户配置
"""


# default config
user_config = {
    'lang': 'en-US',
    'gender': 'Female'
}


def set_config(k, v):
    user_config[k] = v
