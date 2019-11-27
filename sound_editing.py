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

# filepath = '30_times.wav'
# count, snap_frames = snap_count(filepath)
# snap_time = snap_frames_to_time(snap_frames)
# count
# snap_frames
# snap_time
