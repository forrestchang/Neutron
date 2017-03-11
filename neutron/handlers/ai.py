"""Handler for AI service.

这个模块主要用来处理 AI 相关的服务，包括：
- 语义预处理
- 与第三方的 API 交互

TODO:
    - 语义预处理部分

"""

from ..layers.turing import Turing_AI
from . import load_configs


class AIHandler(object):
    """Class for AI handler service.
    """

    def __init__(self):
        configs = load_configs('ai')
        self.ai_service = Turing_AI(**configs['turing'])

    def execute(self, msg):
        """Execute messages from user.

        """
        return self.ai_service.get_response(msg)
