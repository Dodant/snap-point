import librosa
import numpy as np

def snap_count(filepath, hop=500, cp=0.25):
    y, sr = librosa.load(filepath)
    cursor, cnt = 0, 0
    snap_frames = []
    while cursor < len(y):
        if (y[cursor] > cp):
            snap_frames.append(cursor)
            cnt += 1
            cursor += hop
        cursor += 2
    return cnt, snap_frames

def snap_frames_to_time(snap_frames, sr=22050):
    return librosa.core.frames_to_time(snap_frames, sr=sr, hop_length=1)

def cut_samples(filepath):
    y, sr = librosa.load(filepath)
    _, snap_frames = snap_count(filepath)
    sample_ls = []
    for i in snap_frames:
        sample_ls.append(y[i-512:i+513])
    return sample_ls



snap_frames = [512*2]
sd = librosa.core.frames_to_time(snap_frames, sr=22050, hop_length=1)
sd

filepath = '30_times.wav'
ls = cut_samples(filepath)
len(ls)
type(ls)
