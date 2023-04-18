# Snap Point  
2019-2 CNU Econovation ML Project (Team JitterBug) 

### Introduction
SnapPoint is a Python program that uses machine learning to recognize finger snaps and control PowerPoint presentations. 
<br/>This program listens to the surrounding sounds, detects snaps, and performs the desired action using PyAutoGUI.

### Dependencies
To run SnapPoint, you'll need the following Python libraries:

- Librosa: for extracting features from audio data
- PyAudio: for continuous audio input
- PyAutoGUI: for controlling external programs (e.g., PowerPoint)
- TensorFlow and Keras: for machine learning

<br/>You can install these dependencies using pip:

`pip install librosa pyaudio pyautogui tensorflow keras`
## How to Run
1. Ensure that you have all the required dependencies installed.
2. Place the pre-trained model (`ver_1.1.h5`) in the same directory as the script.
3. Run the script with `python snap_point.py` (or replace `snap_point.py` with the name of the script file).
4. The program will start listening to the surrounding sounds and detecting snaps. Once a snap is detected, it will perform the desired action in the PowerPoint presentation.

## Code Overview
The main components of the code include:

1. Loading the pre-trained machine learning model.
2. Setting up an audio stream using PyAudio to listen to the surrounding sounds.
3. Preprocessing the audio data using the Librosa library and the MFCC algorithm.
4. Feeding the preprocessed data into the model and detecting snaps.
5. Performing the desired action using PyAutoGUI when a snap is detected.

## Customization
If you wish to customize the script or train your model, you may need to adjust some of the parameters, such as `CHANNELS`, `RATE`, `FRAMES_PER_BUFFER`, `N_FFT`, `SCREEN_WIDTH`, and `ENERGY_THRESHOLD`. Be sure to adjust these values according to your specific requirements and the capabilities of your system.

## Troubleshooting
If you encounter issues with audio input or output, check your system's audio settings and ensure that the correct audio devices are selected. You may also need to adjust the `FRAMES_PER_BUFFER` and `RATE` parameters to match your audio device's capabilities.

**Note**: This program has been tested with Python 3.7+. If you are using an older version of Python, you may encounter compatibility issues.
