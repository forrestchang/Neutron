from layers.turing import Turing_AI
from . import Handler
import json


class AIHandler(Handler):

    def __init__(self):
        configs = super.load_configs('ai')
        self.ai_service = Turing_AI(**configs['turing'])

    def execute(self, msg):
        return self.ai_service.get_response(msg)
