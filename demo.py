
import os
import time

import librosa
import numpy
import pyaudio
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras import utils

CHANNELS = 1
RATE = 44100
FRAMES_PER_BUFFER = 1024 * 17
N_FFT = 4096
SCREEN_WIDTH = 178
ENERGY_THRESHOLD = 0.4
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
F_LO = librosa.note_to_hz('C2')
F_HI = librosa.note_to_hz('C9')
M = librosa.filters.mel(RATE, N_FFT, SCREEN_WIDTH, fmin=F_LO, fmax=F_HI)
p = pyaudio.PyAudio()
loaded_model = tf.keras.models.load_model('ver_1.1.h5')


def mfcc(y):
    sample = librosa.feature.mfcc(y=y, sr=44100, n_mfcc=40)
    sample = numpy.expand_dims(sample.T,axis=0)
    return sample


def test(sample):
    data = mfcc(sample)
    data = numpy.reshape(data, (-1, data.shape[1], data.shape[2], 1))
    predictions = loaded_model.predict(data)
    if numpy.argmax(predictions) == 0:
        return ''
    elif numpy.argmax(predictions) == 1:
        return 'Snap & Clap'
    else:
        return ''


def generate_string_from_audio(audio_data):

    x_fft = numpy.fft.rfft(audio_data, n=N_FFT)
    melspectrum = M.dot(abs(x_fft))
    char_list = [' ']*SCREEN_WIDTH

    for i in range(SCREEN_WIDTH):
        if melspectrum[i] > ENERGY_THRESHOLD:
            char_list[i] = '*'
        elif i % 30 == 29:
            char_list[i] = '|'
    return ''.join(char_list)


def callback(in_data, frame_count, time_info, status):
    audio_data = numpy.frombuffer(in_data, dtype=numpy.float64)
    print( generate_string_from_audio(audio_data), test(audio_data) )
    frames = []
    for i in range(0, int(RATE / FRAMES_PER_BUFFER * 0.2)):
        data = stream.read(FRAMES_PER_BUFFER)
        frames.append(data)
    return in_data, pyaudio.paContinue


stream = p.open(format=pyaudio.paFloat32,
                channels=CHANNELS,
                rate=RATE,
                input=True,   # Do record input.
                output=False, # Do not play back output.
                frames_per_buffer=FRAMES_PER_BUFFER,
                stream_callback=callback)

stream.start_stream()
while stream.is_active():
    time.sleep(0.100)
stream.stop_stream()
stream.close()
p.terminate()
