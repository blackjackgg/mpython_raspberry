#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 aibot.me, Inc. All Rights Reserved
# 
########################################################################
  
"""
File: gen_wav.py
Date: 2017/03/24 12:36:27
Brief: 通过麦克风录音 生成 wav文件
"""
import machine
import array
import wave
from ulab import numpy as np
import struct
 
 
 
class GenAudio(object):
    def __init__(self):
        self.num_samples = 1000    #pyaudio内置缓冲大小
        self.sampling_rate = 2000  #取样频率
        self.level = 0        #声音保存的阈值
        self.count_num = 0       #count_num个取样之内出现COUNT_NUM个大于LEVEL的取样则记录声音
        self.save_length = 8       #声音记录的最小长度：save_length * num_samples 个取样
        self.time_count = 20        #录音时间，单位s
        self.voice_string = []
 
     
    #保存文件
    def save_wav(self, filename):
        wf = wave.open(filename, 'wb') 
        wf.setnchannels(1) 
        wf.setsampwidth(2) 
        wf.setframerate(self.sampling_rate)
        for i in self.voice_string:
            wf.writeframes(struct.pack('<h',i))
        wf.close()
     
     
    def read_audio(self):
        micpin = machine.Pin(33,machine.Pin.IN)
        mic = machine.ADC(micpin)
        mic.atten(machine.ADC.ATTN_11DB)
         
        save_count = 0
        save_buffer = [] 
        time_count = self.time_count
 
        while True:
            time_count -= 1
             
            # 读入num_samples个取样
            string_audio_data = mic.read() * 1024
            newarray = array.array("H",[])
            for  i  in range(5000):
                newarray.append(mic.read()*1024)
            # 将读入的数据转换为数组
            print("fine")
            audio_data = np.array(newarray)
            #计算大于 level 的取样的个数
            large_sample_count = np.sum(audio_data > self.level)
             
            print(np.max(audio_data)),  "large_sample_count=>", large_sample_count
 
            # 如果个数大于COUNT_NUM，则至少保存SAVE_LENGTH个块
            if large_sample_count > self.count_num:
                save_count = self.save_length
            else: 
                save_count -= 1
            if save_count < 0:
                save_count = 0
             
            if save_count > 0:
                save_buffer.append(string_audio_data)
            else:
                if len(save_buffer) > 0:
                    self.voice_string = save_buffer
                    save_buffer = [] 
                    print("Recode a piece of  voice successfully!")
                    return True
             
            if time_count == 0: 
                if len(save_buffer) > 0:
                    self.voice_string = save_buffer
                    save_buffer = []
                    print("Recode a piece of  voice successfully!")
                    return True
                else:
                    return False
        return True
 
 
 
 
if __name__ == "__main__":
    r = GenAudio()
    r.read_audio()
    r.save_wav("./test.wav")