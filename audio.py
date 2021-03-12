import machine
import utime
import array
from ulab import numpy
import wave
import struct
import socket
import _thread
print("haha")

print("ok")
pcmarray = array.array("H",[0 for x in range(5001)])

wavef = wave.open('22.wav','wb')
wavef.setnchannels(1)
wavef.setsampwidth(2)
wavef.setframerate(2000)
print("wwww")
def wavSetOyt(outpath,pcmarray,rate):

    
#     for val in  pcmarray:
#         val = round(float(val))
#         datastruct = struct.pack('<h',val)
    wavef.writeframesraw(pcmarray)
    
    

# 每次采样的频率都不是固定的 0v-5v 默认是12bit

def micsample():
    global pcmarray
    micpin = machine.Pin(32,machine.Pin.IN)
    mic = machine.ADC(micpin)
    mic.atten(machine.ADC.ATTN_11DB)
    mic.width(machine.ADC.WIDTH_12BIT)
    #默认是12bit的数据
    
    mic16 = mic.read() 
    print(mic16)
    
   
#     start = utime.ticks_us()
#     for i in range(16000):
#         outpath =""
#         recvarray=  struct.pack('<h',mic.read()*1024)
#         wavSetOyt(outpath,recvarray,777)
#     end = utime.ticks_us()
#     duration = end - start
#     rate = 5000 /(duration/1000/1000)
#     print("rate",rate)

#     
#     socketcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     socketcp.connect(("0.0.0.0",60000))
#     socketcp.sendall(pcmarray)
    
    


# def tcplink(conn,addr):
#     recv = b''
#     print("aaa")
#     while 1:
#         data = conn.recv(1000)
#         if not data:
#             break
#         recv += data
#         print(recv)
#         if len(recv) < 3202:
#             continue
#         # 转换
#         print("wtf")
#         recvarray = numpy.frombuffer(recv[0:3202],"uint16")
#         print("ok")
#         rate = recvarray[1600]
#         pcmdate12bit = recvarray[0:1600]
#         
#         pcmdate12bitf = pcmdate12bit.astype(numpy.float32)
#         pcmdate16bitf =  pcmdate12bitf * 16
#         pcmdate16bitf2 =  pcmdate16bitf  - 3276
#         
#         outpath = "C:\\Users\\Administrator\\Desktop\\1.wav"
#         wavSetOyt(outpath ,pcmdate16bitf2,rate )
#     print("shutdown")    
#     conn.close()
#         
# socketcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# socketcp.bind(("0.0.0.0",60000))
# socketcp.listen(100)

# while 1:
#     print("start")
start = utime.ticks_us()
while 1:
    micsample()
    end = utime.ticks_us()
    duration = end - start
    if duration > 300000000 * 1:
        wavef.writeframes(b"")
        wavef.close()
        print("jiesu")
        break
#     conn,addr =socketcp.accept()
#     print(conn,addr)
#     _thread.start_new_thread(tcplink,(conn,addr))
#     print("run")



        
    