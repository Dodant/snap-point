import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np


def get_shape(filepath):
    y, sr = librosa.load(filepath)
    y_mfcc = librosa.feature.mfcc(y=y, sr=sr)
    print("Raw : ", y.shape)
    print("Processed : ". y_mfcc.shape)

def wave_graph(filepath):
    y, sr = librosa.load(filepath)
    plt.figure(figsize=(16, 5))
    librosa.display.waveplot(y, sr=sr)
    plt.show()

def specshow_graph(filepath):
    y, sr = librosa.load(filepath)
    X = librosa.stft(y)
    Xdb = librosa.amplitude_to_db(abs(X))
    plt.figure(figsize=(16, 5))
    librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
    plt.show()

def harm_prec_graph(filepath):
    y, sr = librosa.load(filepath)
    y_harm, y_perc = librosa.effects.hpss(y)
    plt.figure(figsize=(16, 5))
    librosa.display.waveplot(y_harm, sr=sr, alpha=0.25)
    librosa.display.waveplot(y_perc, sr=sr, color='r', alpha=0.5)
    plt.title('Harmonic + Percussive')
    plt.tight_layout()
    plt.show()

def lighten(y_mfcc):
    return np.around(y_mfcc, decimals=2)
