import librosa, pyaudio, time, os, numpy, pyautogui
from tensorflow.keras import models

# Define global variables.
CHANNELS = 1
RATE = 44100
FRAMES_PER_BUFFER = 1024 * 17
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

p = pyaudio.PyAudio()
loaded_model = models.load_model('ver_1.1_mel.h5')

def standardized_mfcc(y):
    sample = librosa.feature.melspectrogram(y=y, sr=44100)
    return numpy.expand_dims(sample.T, axis=0)

def test(sample):
    data = standardized_mfcc(sample)
    predictions = loaded_model.predict(numpy.reshape(data, (-1, data.shape[1], data.shape[2], 1)))
    if numpy.argmax(predictions) == 0:
        pyautogui.press('space')
        print("Snap")
        time.sleep(0.1)
    elif numpy.argmax(predictions) == 1:
        pyautogui.keyDown('shift')
        pyautogui.press('n')
        pyautogui.keyUp('shift')
        print("Clap")
        time.sleep(0.1)
    else :
        return

def callback(in_data, frame_count, time_info, status):
    test(numpy.frombuffer(in_data, dtype=numpy.float64))
    return in_data, pyaudio.paContinue

stream = p.open(rate=RATE,
                channels=CHANNELS,
                format=pyaudio.paFloat32,
                input=True, output=False, # Do record input. Do not play back output.
                frames_per_buffer=FRAMES_PER_BUFFER,
                stream_callback=callback)

stream.start_stream()
print("running")
while stream.is_active():
    time.sleep(0.100)
stream.stop_stream()
stream.close()
p.terminate()
