# -*- coding: utf-8 -*-
from app import app
from flask import request, jsonify

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
    f.save('./upload/'+f.filename)
    #voice = open(FAKE_VOICE)
    return jsonify(
        {
            'code': 0,
            'message': 'ok'
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

