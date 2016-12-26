import numpy as np
from pyaudio import PyAudio, paInt16
from datetime import datetime
import wave


# define of params
NUM_SAMPLES = 2000
framerate = 8000
channels = 1
sampwidth = 2
# record time
TIME = 10


def save_wave_file(filename, data):
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(framerate)
    wf.writeframes(b''.join(data))
    wf.close()


def record_wave():
    # open the input of wave
    pa = PyAudio()
    stream = pa.open(
        format=paInt16,
        channels=1,
        rate=framerate,
        input=True,
        frames_per_buffer=NUM_SAMPLES
    )
    save_buffer = []

    # if record is end
    is_end = True

    while True:
        # read NUM_SAMPLES sampling data
        string_audio_data = stream.read(NUM_SAMPLES)

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
            save_wave_file(filename, save_buffer)
            print(filename + ' saved')
            is_end = False
            save_buffer = []
        print('=====')


if __name__ == '__main__':
    record_wave()
