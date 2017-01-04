from . import app
from flask import request, jsonify, send_from_directory
from .handlers.ai import AIHandler
from .handlers.audiotext import AudioTextHandler


@app.route('/')
def index():
    return 'Test Page'


@app.route('/upload_audio', methods=['POST'])
def upload_audio():
    audio_text_handler = AudioTextHandler()
    ai_handler = AIHandler()
    f = request.files['audio']
    recognize_result = audio_text_handler.audio2text(f)
    if recognize_result == 'fail':
        save_file_name = audio_text_handler.text2audio('你在说什么鬼')
    else:
        print("Recognize result: {}".format(recognize_result))
        resp_message = ai_handler.execute(recognize_result)
        print("Respond message: {}".format(resp_message))
        save_file_name = audio_text_handler.text2audio(resp_message)
    return jsonify(
        {
            'code': 0,
            'message': 'ok',
            'recognize_result': recognize_result,
            'save_file_name': save_file_name
        }
    )


@app.route('/audio/<filename>')
def get_audio(filename):
    return send_from_directory(
        directory='return_audio',
        filename=filename
    )
