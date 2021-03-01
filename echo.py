import utime
from machine import Pin

trig, echo = Pin(19,Pin.OUT),Pin(5,Pin.IN)
trig.value(0)
echo.value(0)

red=Pin(27, Pin.OUT) #port 2 is used for led
green =Pin(12, Pin.OUT)
blue=Pin(14, Pin.OUT)

def checkdist():
    trig.value(1)
    utime.sleep(0.00001)
    trig.value(0)
    while(echo.value()==0):
        pass
    t1 = utime.ticks_us()
    while(echo.value()==1):
        pass
    t2 = utime.ticks_us()
    t3 = utime.ticks_diff(t2,t1)/10000
    return t3*340/2

try:
    while 1:
        dist = checkdist()
        print("distance:%0.2f cm" %dist)
        if dist < 10:
            print("too close")
            red.on()
            green.off()
        else:
            green.on()
            red.off()
        utime.sleep(0.5)
except KeyboardInterrupt:
    pass
    