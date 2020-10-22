# -*- coding: utf-8 -*-

from pydub import AudioSegment
import pyaudio
import time
import threading
import wave
import numpy as  np
import matplotlib.pyplot as plt
import math


class Recorder():
    def __init__(self, chunk=1024, channels=1, rate=64000):
        self.CHUNK = chunk
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = channels
        self.RATE = rate
        self._running = True
        self._frames = []

    def start(self):
        self.__recording()

    def __recording(self):
        self._running = True
        self._frames = []
        p = pyaudio.PyAudio()
        stream = p.open(format=self.FORMAT,channels=self.CHANNELS,rate=self.RATE,input=True,frames_per_buffer=self.CHUNK)
        while (self._running):
            begin1 = time.time()
            t = 0;
            while(t<=0.1):
                fina1 = time.time()
                t = fina1 - begin1
                data = stream.read(self.CHUNK)
                self._frames.append(data)

            stream.stop_stream()
            stream.close()
            p.terminate()
            rec.save("100.wav")
            self._running = False

    def stop(self):
        self._running = False

    def save(self, filename):

        p = pyaudio.PyAudio()
        if not filename.endswith(".wav"):
            filename = filename + ".wav"
        wf = wave.open(filename, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self._frames))
        wf.close()
        # print("Saved")

    def control(self):
        a = int(input('输入2关闭:'))
        return a


if __name__ == "__main__":
    a = int(input('请输入相应数字开始:'))
    begin = time.time()
    plt.ion()
    plt.figure(1)
    time_list = []
    sound_list = []
    db  = 0
    while (a==1):
        rec = Recorder()
       # threading._start_new_thread(rec.control, ())
       # a = rec.control()
       # if a == 1:

        #begin = time.time()
        #print("Start recording")
        rec.start()
        sound = AudioSegment.from_file("100.wav", "wav")
        # # 取得音频的分贝数
        # loudness = sound.dBFS
        # print(loudness)
        # # 获取音频音量大小，该值通常用来计算分贝数（dB= 20×lgX）
        loudness = sound.rms
        raf = sound.max_dBFS
        db = math.log(loudness,10) * 20
        sound_list.append(db)

        fina = time.time()

        time_list.append(fina - begin)


        plt.plot(time_list, sound_list, c='r', ls='-', marker='o', mec='b', mfc='w')  ## 保存历史数据
        # plt.plot(t, np.sin(t), 'o')
        plt.pause(0.1)

        print(db)

           # b = int(input('请输入相应数字停止:'))
          #  if b == 2:
          #      print("Stop recording")
          #      rec.stop()
         #       fina = time.time()
          #      t = fina - begin
           #     print('录音时间为%ds' % t)
           #     rec.save("1_%d.wav" % i)