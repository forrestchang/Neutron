from app import app
from flask import request, jsonify, send_from_directory
from .baidu_api import recognize

@app.route('/')
def index():
    return 'Test Page'


@app.route('/upload_voice', methods=['POST', 'GET'])
def upload_voice():
    # f = open('app/hello.wav', 'rb')
    f = request.files['voice']
    recognize_result = recognize(f)
    print("Recognize result: {}".format(recognize_result))
    return jsonify(
        {
            'code': 0,
            'message': 'ok',
            'recognize_result': recognize_result
        }
    )


@app.route('/voice/<filename>')
def get_voice(filename):
    return send_from_directory(
        directory='return_voice',
        filename=filename
    )
