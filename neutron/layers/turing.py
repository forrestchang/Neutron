"""This module used for process requests from turing API.
"""

import uuid
import requests


class Turing_AI(object):
    """Turing_AI service.
    """

    def __init__(self, **kwargs):
        self.url = 'http://www.tuling123.com/openapi/api'
        self.access_key = kwargs['access_key']
        self.userid = uuid.uuid1().hex

    def get_response(self, msg):
        """Get response from http://www.tuling123.com/openapi/api

        Args:
            msg (str): message you want to use Turing_AI API to process.

        Returns:
            str: result after processing text you sent by Turing_AI
        """
        msg_json = {
            "key": self.access_key,
            "info": msg,
            "userid": self.userid
        }
        resp = requests.post(self.url, json=msg_json)
        return resp.json()['text']
