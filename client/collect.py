import numpy as np
from pyaudio import PyAudio, paInt16
from datetime import datetime
from pygame import mixer
import requests
import wave
import os
import time
import shutil

SERVER_URL = os.getenv('SERVER_URL') or '0.0.0.0'

NUM_SAMPLES = 2**12
FRAMERATE = 8000
CHANNELS = 1
SAMPWIDTH = 2


def save_wave_file(filename, data):
    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(SAMPWIDTH)
    wf.setframerate(FRAMERATE)
    wf.writeframes(b''.join(data))
    wf.close()


def record_wave():
    # open the input of wave
    pa = PyAudio()
    stream = pa.open(
        format=paInt16,
        channels=CHANNELS,
        rate=FRAMERATE,
        input=True,
        frames_per_buffer=NUM_SAMPLES
    )
    save_buffer = []

    # if record is end
    is_end = True

    while True:
        # read NUM_SAMPLES sampling data
        string_audio_data = stream.read(NUM_SAMPLES, exception_on_overflow=False)

        wave_data = np.fromstring(string_audio_data, dtype=np.short)
        wave_data.shape = -1, 2
        wave_data = wave_data.T
        print(len(wave_data[0]))
        print(np.mean(np.abs(wave_data[0])))

        if np.mean(np.abs(wave_data[0])) > 1200:
            is_end = False
        elif np.mean(np.abs(wave_data[0])) < 700:
            is_end = True

        if is_end is False:
            save_buffer.append(string_audio_data)
            print(len(save_buffer))

        if len(save_buffer) != 0 and is_end is True:
            filename = datetime.now().strftime("%Y-%m-%d_%H_%M_%S") + '.wav'
            save_wave_file('records/' + filename, save_buffer)

            files = {
                "voice": open('records/' + filename, 'rb')
            }
            resp = requests.post(
                "http://" + SERVER_URL + ":5000/upload_voice",
                files=files
            )
            if resp.json()['code'] == 0:
                print(resp.json()['recognize_result'])
                r = requests.get(
                    "http://" + SERVER_URL + ":5000/voice/" + resp.json()['save_file_name'],
                    stream=True
                )
                with open('temp.mp3', 'wb') as f:
                    for data in r.iter_content(chunk_size=1024):
                        f.write(data)
                # stream.stop_stream()
                mixer.init()
                mixer.music.load('temp.mp3')
                mixer.music.play()
                time.sleep(2)
                # stream.start_stream()

            print(filename + ' saved')
            is_end = False
            save_buffer = []
        print('=====')


if __name__ == '__main__':
    record_wave()
