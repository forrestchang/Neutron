# -*- coding: utf-8 -*-
from app import app
from flask import request, jsonify, send_from_directory
from azure_api import recognize, synthesize

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
    # 获得语音文字信息
    recognize_result = recognize(f)
    # 获得返回文字信息
    return_text = recognize_result
    # 获得返回语音信息
    is_succeed, save_file_name = synthesize(return_text)
    print recognize_result
    print is_succeed
    print save_file_name
    return jsonify(
        {
            'code': 0,
            'message': 'ok',
            'recognize_result': recognize_result,
            'save_file_name': save_file_name
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


@app.route('/voice/<file_name>', methods=['GET'])
def get_voice(file_name):
    """
    返回声音文件
    """
    return send_from_directory(
        directory="return_voice",
        filename=file_name
    )
