import machine
import utime
import array
import wave
import numpy
import struct
import socket
import _thread

pcmarray = array.array("H",[0 for x in range(16001)])

def wavSetOyt(outpath,pcmarray,rate):
    wavef = wave.open(path,'wb')
    wavef.setnchannels(1)
    wavef.setsamplewidth(2)
    wavef.setframerate(rate)
    
    for val in  pcmarray:
        val = round(float(val))
        datastruct = struct.pack('<h',val)
        wavef.write(datastruct)
    wavef.writeframes(b"")
    wavef.close()
    
    


def micsample():
    global pcmarray
    micpin = machine.Pin(33,machine.Pin.IN)
    mic = machine.ADC(micpin)
    mic.atten(machine.ADC.ATTN_11DB)
    
    start = utime.ticks_us()
    for i in range(16000):
        pcmarray[i] = mic.read()
    end = utime.ticks_us()
    duration = end - start
    print(duration)
    rate = 16000 /(duration/1000/1000)
    print(rate)
    pcmarray[16000] = int(rate)
    
    socketcp = socket.socket(socket.AF_INET,socket.SOCKET_STREAM)
    socketcp.connect(("127.0.0.1",60000))
    socketcp.sendall(pcmarray)
    
    


def tcplink(conn,addr):
    recv = b''
    while 1:
        data = conn.recv(1000)
        if not data:
            break
        recv += data
        if len(recv) <32002:
            continue
        # 转换
        recvarray = numpy.formbuffer(recv[0:32002],"uint16")
        rate = recvarray[16000]
        pcmdate12bit = recvarray[0:16000]
        
        pcmdate12bitf = pcmdate12bit.astype(numpy.float32)
        pcmdate16bitf =  pcmdate12bitf * 16
        pcmdate16bitf2 =  pcmdate16bitf  - 32768
        
        outpath = "C:\\Users\\Administrator\\Desktop\\1.wav"
        wavSetOyt(outpath ,pcmdate16bitf2,rate )
    conn.close()
        
socketcp = socket.socket(socket.AF_INET,socket.SOCKET_STREAM)
socketcp.bind(("0.0.0.0",60000))
socketcp.listen(100)
while 1:
    conn,addr =socketcp.accept()
    _thread.start_new_thread(tcplink,(conn,addr))

        
    