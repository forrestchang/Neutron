# -*- coding: utf-8 -*-
from app import app
from flask import request, jsonify, send_from_directory
from azure_api import recognize, synthesize, emotion_recognize
from voice_handler import handle_voice


FAKE_VOICE = "hello.mp3"


@app.route('/')
def test():
    return "hello world"


@app.route('/upload_voice', methods=['POST'])
def upload_voice():
    """
    接收一段语音 返回处理结果
    """
    f = request.files['voice']
    # 获得语音文字信息
    recognize_result = recognize(f)
    # 获得返回文字信息
    print "recognize_result", recognize_result.encode("utf-8")
    return_text = handle_voice(recognize_result)
    print "return text", return_text.encode("utf-8")
    # 获得返回语音信息
    is_succeed, save_file_name = synthesize(return_text)
    return jsonify(
        {
            'code': 0,
            'message': 'ok',
            'recognize_result': recognize_result,
            'save_file_name': save_file_name
        }
    )


@app.route('/upload_image', methods=['POST'])
def upload_image():
    """
    接收一张图片 返回处理结果
    """
    f = request.files['image']
    # 获得语音文字信息
    recognize_result = emotion_recognize(f)
    return jsonify(
        {
            'code': 0,
            'message': 'ok',
            'emotion': recognize_result
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


@app.route('/image/<file_name>', methods=['GET'])
def get_image(file_name):
    """
    返回图片文件
    """
    return send_from_directory(
        directory="image",
        filename=file_name
    )
