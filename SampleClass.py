import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import os # 파일 로드를 위해서 넣음
import glob # 정규식 사용가능하게 하는 라이브러리

# sampling rate = 22050
# 추후 변경 예정

class SoundSample:

    def __init__(self, filepath):
        self.filepath = filepath
        self.y, self.sr = librosa.load(filepath)
        self.cnt, self.snap_frames = snap_count(filepath)

    # 한 음성파일에 대한 기본적인 정보를 출력
    def basic_info(self):
        duration = librosa.get_duration(y=y, sr=sr)
        print('File Name :', filepath)
        print('File Duration :', duration)
        print('Sampling Rate :', sr)
        print('# of Samples :', len(y))

    def normal_graph(self, fig_x, fig_y):
        plt.figure(figsize=(fig_x,fig_y))
        plt.plot(y)
        x_ticks = np.array([i for i in range(0,len(y),(sr/4))])
        y_ticks = np.array([i for i in range(-int(np.max(y)*100),int(np.max(y)*100),5)])
        plt.xticks(x_ticks, (x_ticks/sr), rotation=45) # x가 0.25초씩 보임
        plt.yticks((y_ticks/100)) # y가 양수 0.25씩 보임
        plt.show()

    def bing(self, fig_x=14, fig_y=5):
        basic_info()
        normal_graph(fig_x, fig_y)

    # 핑거스냅한 y배열의 위치를 찾아내 스냅 수와 y배열의 위치를 담은 배열을 리턴
    def snap_count(self, hop=500, cp=0.25):
        cursor, cnt = 0, 0
        snap_frames = []
        while cursor < len(y):
            if (y[cursor] > cp):
                snap_frames.append(cursor)
                cnt += 1
                cursor += hop
            cursor += 2
        return cnt, snap_frames

    # 스냅의 위치들(y)를 시간으로 변환한 배열을 리턴한다.
    @staticmethod
    def snap_frames_to_time(snap_frames, sr=22050):
        return librosa.core.frames_to_time(snap_frames, sr=sr, hop_length=1)

    # 스냅을 친 부분의 앞뒤 512씩 짤라 2차원 배열에 담는다.
    def cut_samples(self):
        sample_ls = []
        for i in snap_frames:
            sample_ls.append(y[i-512:i+513])
        return sample_ls

    def cutting_file_sound(self, range_len, fig_x, fig_y):
        cnt = 1 # 인덱스 확인
        bing(fig_x, fig_y)
        critical_point = float(input("Critical point: ")) # 임계값 입력

        i = 0
        while i < len(y):
            if y[i]>critical_point: # 임계값을 넘기면 0.125초 범위내의 argmax 구함
                tmp = int(i + 0.125 * sr)
                center = i + np.argmax(y[i:tmp])
                starting_point = int(center - range_len*sr) # armax 기준 입력한 파라미터 +-범위 자름
                ending_point = int(center + range_len*sr)
                if starting_point<0: # - 범위가 인덱스 밖이면 컨티뉴
                    i = ending_point
                    continue
                elif ending_point > len(y): # + 범위가 인덱스 밖이면 컨티뉴
                    continue
                plt.figure(figsize=(30,16)) # 시각화
                sound = y[starting_point:ending_point] # 데이터셋에 넣음
                librosa.display.waveplot(sound, sr=sr)
                plt.title("#{}     {} second".format(cnt,s/sr))
                plt.ylim(1,-1)
                plt.show()

                data = np.concatenate((train, np.expand_dims(sound, axis=0)), axis=0)
                i = en
                cnt += 1
            i += 1
        return data # 정제된 데이터 리턴

    def cutting_dir_sound(directory, a, length_a=30):
        batch_size = 0
        data_length = int(2*a*44100)
        train = np.zeros((batch_size, data_length)) # 데이터셋 형식
        file_list = glob.glob(fpath + '*.wav') # 디렉토리 안 모든 파일로드
        cnt = 1
        for file in file_list:
            temp = cutting_file_sound()
            listSound = np.expand_dims(temp, axis=0) # 데이터셋에 넣음
            train = np.concatenate((train,temp), axis=0)
            cnt += 1
        return train # 모든 데이터를 담은 데이터셋 리턴
