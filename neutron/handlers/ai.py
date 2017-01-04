from ..layers.turing import Turing_AI
from . import load_configs
import json


class AIHandler(object):

    def __init__(self):
        configs = load_configs('ai')
        self.ai_service = Turing_AI(**configs['turing'])

    def execute(self, msg):
        return self.ai_service.get_response(msg)
