import machine
from machine import ADC
import utime
import array
from ulab import numpy
import wave
import struct
import socket
import _thread
from machine import Timer


print("ok")
wavef = wave.open('qq.wav','wb')
wavef.setnchannels(1)
wavef.setsampwidth(2)
caiyangrate = int(48 * 1000) # 人声 800hz  录音机用8000 采样率高于原来频率两倍就可以采样还原出来
framerate  =  (1 / (caiyangrate) )*1000 * 1000 * 100 #  这里是固定1600 
voiceup = 5 # 声音增益倍数  倍数太大声音直接没了！！ 调高检测阈值 使用放大倍数
wavef.setframerate(framerate )

micpin = machine.Pin(34,machine.Pin.IN)
print(micpin.value())
print(micpin.value())
mic = machine.ADC(micpin)
mic.atten(machine.ADC.ATTN_11DB)
mic.width(ADC.WIDTH_12BIT)

mctimer = Timer(1)
pccount = 0
pcmarray = array.array('H',[])


def savewav(data):
    datastruct = struct.pack('h',data) # 普通记录用i 不行改h
    wavef.writeframesraw(datastruct)

#每次采样的频率都不是固定的 0v-5v 默认是12bit
    # 需要调麦克风灵敏度 蓝色方块上面的旋钮
    
def micread(timer):
    global mic
    global pcmarray
    global mctimer
    global pccount
    
    data = (mic.read()  * 16 ) - 32767 # 校正值
    savewav(data * 10)
    
    if pccount > 4798:
        print("跳出")
        mctimer.deinit()
    else:
        pccount+=1
        


def micsample():
    # 读取麦克风callback函数
    global mic
    global pcmarray
    global mctimer
    global pccount
    
    data = (mic.read()  * 16 ) - 32767 # 校正值  16位 2^16 取中间值
    pcmarray.append(data * voiceup) # 声音波形放大
    us = int( (1 / (caiyangrate * 2) )*1000 * 1000)
    utime.sleep_us(us)   # 间隔的秒数 = (1 / (采样频率 * 2) )*1000 * 1000
#     savewav(data * 10)
    
#     startime = utime.ticks_us()
#     mctimer.init(mode=machine.Timer.PERIODIC,callback=micread,freq=4000)
#     while pccount  < 4798: # 设置一共采样多久
#         continue
    
    


#     endtime = utime.ticks_us()
#     duration = endtime - startime
#     rate = 16000 /(duration/1000/1000)


#     mic16 = (mic.read()  * 16 ) - 32767
#     print(mic16)

start = utime.ticks_ms()
while 1:
    end = utime.ticks_us()
    if utime.ticks_diff(utime.ticks_ms(), start) > 5000 *1:
        wavef.writeframes(b"")
        print("jiesusample")
        break
    micsample()
# print(pcmarray)

for i in pcmarray:  
    savewav(i)
# 保存文件单独处理 不然采样率跟不上！
print("end")
wavef.close()
# def micsample2():
#     #默认是12bit的数据
#     print(mic.read())
# while 1:
#   micsample2()
#   utime.sleep(1)
# 往左边旋转调高阈值  使得灯刚好暗掉 稍微说话灯就能亮
       