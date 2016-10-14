# -*- coding: utf-8 -*-
from app import app
from flask import request, jsonify
from azure_api import recognize

FAKE_VOICE = "hello.mp3"


@app.route('/')
def test():
    return "hello world"


@app.route('/upload_voice', methods=['POST'])
def upload_voice():
    """
    接收一段语音 返回处理结果
    """
    # file = request.files['file']
    f = request.files['voice']
    # f.save('./upload/'+f.filename)
    recognize_result = recognize(f)
    print recognize_result
    return jsonify(
        {
            'code': 0,
            'message': 'ok',
            'recognize_result': recognize_result
        }
    )


@app.route('/upload_image')
def upload_image():
    """
    接收一张图片 返回处理结果
    """
    return jsonify(
        {
            'code': 0,
            'message': 'ok'
        }
    )

