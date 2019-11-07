import librosa
import numpy as np

def basic_info(filepath):
    y, sr = librosa.load(filepath, sr=40000)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)
    duration = librosa.get_duration(y=y, sr=sr)
    print('File Name :', filepath)
    print('File Duration :', duration)
    print('Sampling Rate :', sr)
    print('# of Samples :', len(y))
    print('Beat Times :', len(beat_times))
    print(beat_times)
