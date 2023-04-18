"""
musicinformationretrieval.com/realtime_spectrogram.py
PyAudio example: display a live log-spectrogram in the terminal.
For more examples using PyAudio:
    https://github.com/mwickert/scikit-dsp-comm/blob/master/sk_dsp_comm/pyaudio_helper.py
"""
import librosa
import numpy as np
import pyaudio
import time

# Define global variables.
CHANNELS = 1
RATE = 11025
FRAMES_PER_BUFFER = 1000
N_FFT = 4096
SCREEN_WIDTH = 178
ENERGY_THRESHOLD = 0.4

# Choose the frequency range of your log-spectrogram.
F_LO = librosa.note_to_hz('C2')
F_HI = librosa.note_to_hz('C9')
M = librosa.filters.mel(RATE, N_FFT, SCREEN_WIDTH, fmin=F_LO, fmax=F_HI)

p = pyaudio.PyAudio()

def generate_string_from_audio(audio_data):
    """
    This function takes one audio buffer as a numpy array and returns a
    string to be printed to the terminal.
    """
    # Compute real FFT.
    # x_fft = np.fft.rfft(audio_data, n=N_FFT)
    # Compute mel spectrum.
    # melspectrum = M.dot(abs(x_fft))
    # Initialize output characters to display.
    # char_list = [' ']*SCREEN_WIDTH

    mfcc = librosa.feature.mfcc(audio_data, sr=RATE)
    mfcc = np.argmax(mfcc.T, axis=1)

    return max(mfcc)

def callback(in_data, frame_count, time_info, status):
    audio_data = np.fromstring(in_data, dtype=np.float32)
    i = generate_string_from_audio(audio_data)
    print(" "*i, i)
    return (in_data, pyaudio.paContinue)

stream = p.open(format=pyaudio.paFloat32,
                channels=CHANNELS,
                rate=RATE,
                input=True,   # Do record input.
                output=False, # Do not play back output.
                frames_per_buffer=FRAMES_PER_BUFFER,
                stream_callback=callback)

stream.start_stream()
while stream.is_active():
    time.sleep(0.010)
stream.stop_stream()
stream.close()

p.terminate()
