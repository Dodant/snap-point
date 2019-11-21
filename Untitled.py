import librosa
import numpy as np

y, sr = librosa.load('30_times.wav', sr=44100)
y_mfcc = librosa.feature.mfcc(y, sr=44100)
print(y_mfcc)
