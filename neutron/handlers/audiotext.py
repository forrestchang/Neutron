from layers.baidu import BaiduService
import json


class AudioTextHandler(Handler):

    def __init__(self):
        configs = super.load_configs('voice')
        self.audio_text_service = BaiduService(**configs['baidu'])

    def audio2text(self, audio_file):
        return self.audio_text_service.audio2text(audio_file)

    def text2audio(self, text):
        is_succeed, save_file_name = self.audio_text_service.text2audio(text)
        if is_succeed == 'ok':
            return save_file_name
        else:
            return None
