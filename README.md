# Noise-monitoring-procedures
基于树莓派的噪音监测系统
通过麦克风录音,获取音频文件再对音频文件进行声音大小分析,将其可视化展示

2020.10.23 噪音检测系统 alpha 0.0.1 demo

开发环境 :
1.系统:Windows 10
2.语言开发版本:Python 3.9
3.第三方库依赖:
from pydub import AudioSegment
import pyaudio
import time
import wave
import matplotlib.pyplot as plt
import math
4.默认麦克风

使用说明 :
1.配置环境
2.下载程序 "实时声音可视化.py"
3.配置默认麦克风
4.在环境下运行程序
