# Snap Point

## Team & Project Introduction

안녕하세요~ 저희는 18기 신입 오중균, 김창영으로 이루어진 팀 **JitterBug**입니다. 
이번 학기에 에코노베이션 머신러닝 프로젝트를 진행하게 되었습니다.

프로젝트명은 **SnapPoint**인데요. 
손가락을 튕기는 행위인 Snap과 PowerPoint의 Point를 합쳐서 만든 이름입니다. 
이름에서도 알 수 있듯이, Finger Snap으로 PowerPoint를 제어하는 것이 프로젝트의 목표입니다. 

## Motivation
[프레젠테이션 제어]를 위한 핑거스냅 기반 인터페이스
* 핑거스냅의 편의성
* 청중의 집중도 향상
* 발표자의 개성 표출

## Data
머신러닝에서 가장 중요한 것은 역시나 데이터입니다.
이 프로젝트는 소리를 이용하므로 당연히 음성 데이터가 필요하겠죠?
저희 프로젝트에 관심을 가져 주신 여러분들의 도움으로 총 12명이 참여해 약 1000개의 데이터를 수집할 수 있었습니다.
이 1000개의 데이터만으로는 모델 학습에 부족함이 있어, 데이터 증강 기법(Data Augmentation)을 활용했습니다.
음의 높이를 조절하는 방식과 노이즈를 섞는 방식으로 2000개의 추가 데이터를 생성해 총 3000개의 데이터를 확보했습니다.

이 데이터들을 바로 모델에 넣어주면 안 됩니다. 데이터 전처리(Preprocessing) 과정을 거쳐야 합니다.
모델 성능에 직접적인 영향을 미치는 중요한 과정입니다. 음성 데이터의 특성을 추출할 때 주로 사용하는 Librosa의 **MFCC** 알고리즘을 이용하여 전처리를 수행했습니다.

## Libraries
음성 데이터의 특징을 추출하기 위한 **Librosa**,
소리를 지속적으로 수신하기 위한 **PyAudio**,
외부 프로그램을 제어하기 위한 **PyAutoGUI**,
그리고 머신러닝에 주로 사용되는 **TensorFlow와** **Keras**를 활용했습니다.

## Making Model
```python
model = tf.keras.models.Sequential()
model.add(Conv2D(32, kernel_size, padding='same', input_shape=(18,128,1)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=pool_size))
model.add(Dropout(0.5))

model.add(Conv2D(64, kernel_size, padding='same'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=pool_size))
model.add(Dropout(0.5))

model.add(Conv2D(128, kernel_size, padding='same'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=pool_size))
model.add(Dropout(0.5))

model.add(Flatten())
model.add(Dense(600))
model.add(Activation('relu'))
model.add(Dropout(0.5))

model.add(Dense(10))
model.add(Activation('softmax'))

model.compile(optimizer= 'adam', loss='categorical_crossentropy', metrics = ['accuracy'])
```

프로그램의 작동 원리는 매우 간단합니다.
먼저 프로그램이 시작되면 미리 생성해 둔 머신러닝 모델을 불러와서 로드합니다.
모델이 로드되면 PyAudio를 이용하여 프로그램이 주변 소리를 듣도록 스트림을 실행시킵니다.
스트림이 작동하는 동안 수집된 음성 데이터를 빠르게 처리(전처리)하여 모델에 입력할 수 있게 합니다.
따라서 스냅이 발생하는 순간, 전처리된 데이터가 모델에 들어가 스냅이 맞다고 판단하면 PyAutoGUI를 통해 우리가 원하는 동작을 수행하게 됩니다.

## Usage
	1. 실행시킨다.
	2. 활용하고자 하는 프로그램(e.g. Youtube)에 포커스를 준다
	3. Snap (핑거스냅을 못하는 사람은 박수소리로 제어해도 무관)

## Also you can control
	* YouTube, Netflix, Music Player - Toggle Play & Pause
	* YouTube, Music Player - Next Video, Next Track
	* PowerPoint, Keynote - Next Slide

## Further Possible Application
	* Snap Beeper : 열쇠, 리모콘, 에어팟등과 같이 잃어버리는 쉬운 물건에 작은 기기를 달아서 손가락을 튕기면 소리가 울리게 하여 위치를 알림.
	* Snap Snoozer : 좀만 더 자고 싶을때 손가락을 튕기면 몇분동안 Snooze 되게 함. 

