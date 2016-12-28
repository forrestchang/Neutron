from layers.turing import Turing_AI
import json


class AIHandler(object):

    def __init__(self):
        configs = json.loads(open('config.json').read())
        self.ai_service = Turing_AI(**configs['turing'])

    def execute(self, msg):
        return self.ai_service.get_response(msg)
