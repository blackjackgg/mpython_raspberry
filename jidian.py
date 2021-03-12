# 继电器
from machine import Pin,PWM
import utime

jidian = Pin(17, Pin.OUT)
jidian.on()
utime.sleep(5)
print("turnoff")
jidian.off()