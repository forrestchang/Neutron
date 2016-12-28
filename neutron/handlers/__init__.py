import json


class Handler(object):

    def __init__(self):
        pass

    def load_configs(self, func):
        with open('neutron.json') as f:
            configs = json.loads(f.read())
        return configs[func]
