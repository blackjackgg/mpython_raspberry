'''
ESP32串口通信-字符串数据自发实验

接线 将开发板的 13号引脚与12号引脚用杜邦线相连接。

'''
from machine import UART,Pin
import utime

# 初始化一个UART对象
uart = UART(2, baudrate=9600, rx=14,tx=12,timeout=10)
# rx tx 端口号是反过来的  https://www.cirmall.com/bbs/thread-102657-1-1.html

# esp32 有效的gpio脚 0，2，4，5，9，10， 12-19， 21-23，25， 26， 34-36， 39

from microgps import MicropyGPS
my_gps = MicropyGPS(8)

while True:
    if uart.any():
        # 如果有数据 读入一行数据返回数据为字节类型
        # 例如  b'hello 1\n'
        bin_data = uart.readline()
        # 将手到的信息打印在终端
        print(bin_data.decode())