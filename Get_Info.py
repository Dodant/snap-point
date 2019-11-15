import librosa
import librosa.display
import IPython.display as ipd
import matplotlib.pyplot as plt
import numpy as np

# Sampling Rate = 20000
# Hop Length = 500
# n_MFCC = 40
# 10 Frame
# Data Augmentation = (+0.1, +0.5, +1.0, -0.1, -0.5, -1.0)

# 파일의 기본정보들을 보여준다. 파일명, 파일시간 등


def basic_info(filepath):
    # 샘플링 레이트는 슬라이싱을 편하게 하기 위해 20000으로 설정
    # 핑거스냅소리를 비트로 인식하여 beat_times으로 친 시간들이 나옴
    y, sr = librosa.load(filepath, sr=20000)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr, hop_length=500)
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)
    duration = librosa.get_duration(y=y, sr=sr)
    print('File Name :', filepath)
    print('File Duration :', duration)
    print('Sampling Rate :', sr)
    print('# of Samples :', len(y))
    print('Beat Times :', len(beat_times))
    print(beat_times)

def get_shape(filepath):
    y, sr = librosa.load(filepath, sr=20000)
    y_mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40, hop_length=500)
    print("Raw : ", y.shape)
    print("Processed : ". y_mfcc.shape)

def wave_graph(filepath):
    y, sr = librosa.load(filepath, sr=20000)
    plt.figure(figsize=(14, 5))
    librosa.display.waveplot(y, sr=sr)
    plt.show()

def specshow_graph(filepath):
    y, sr = librosa.load(filepath, sr=20000)
    X = librosa.stft(y)
    Xdb = librosa.amplitude_to_db(abs(X))
    plt.figure(figsize=(14, 5))
    librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
    plt.show()

def harm_prec_graph(filepath):
    y, sr = librosa.load(filepath, sr=20000)
    y_harm, y_perc = librosa.effects.hpss(y)
    plt.figure(figsize=(14, 5))
    librosa.display.waveplot(y_harm, sr=sr, alpha=0.25)
    librosa.display.waveplot(y_perc, sr=sr, color='r', alpha=0.5)
    plt.title('Harmonic + Percussive')
    plt.tight_layout()
    plt.show()

def lighten(y_mfcc):
    return np.around(y_mfcc, decimals=2)
