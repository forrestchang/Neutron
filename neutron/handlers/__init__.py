import json

js = """{
  "voice":
  {
    "baidu": {
      "client_id": "U0Fzj0kga5prC6wxDMpgNONA",
      "client_secret": "efeeca301934f987b28c1ae6b9105d8c"
    }
  },

  "ai":
  {
    "turing": {
      "access_key": "fb583eb0d6a54e758489e971ec2f3aed"
    }
  }
}"""


def load_configs(func):
    # TODO: read configs from file
    # with open('../.neutron.d/init.json') as f:
    #     configs = json.loads(f.read())
    configs = json.loads(js)
    return configs[func]
