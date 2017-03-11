"""Handler for audio to text service.

"""

from ..layers.baidu import BaiduService
from . import load_configs
import json


class AudioTextHandler(object):
    """Class for audio-text service.

    """

    def __init__(self):
        configs = load_configs('voice')
        self.audio_text_service = BaiduService(**configs['baidu'])

    def audio2text(self, audio_file):
        """Convert audio file to text.
        Args:
            audio_file (file stream)

        Returns:
            str: audio to text

        """
        return self.audio_text_service.audio2text(audio_file)

    def text2audio(self, text):
        """Convert text to audio file.

        params:
        -------
        text: string text

        return:
        -------
        file stream: open('temp.mp3', 'rb')
        """
        is_succeed, save_file_name = self.audio_text_service.text2audio(text)
        if is_succeed == 'ok':
            return save_file_name
        else:
            return None
