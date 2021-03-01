from machine import Pin,PWM
import utime

 
red=Pin(12, Pin.OUT) #port 2 is used for led
green =Pin(14, Pin.OUT)
blue=Pin(27, Pin.OUT)

pwmr = PWM(red)
pwmr.freq(500)

pwmb = PWM(blue)
pwmb.freq(1500)

pwmg = PWM(green)
pwmg.freq(600)

while True:
    for duty in range(0,1023, 80):
        pwmr.duty(duty)
        utime.sleep_ms(60)
    for duty in range(1023, 0,-50):
        pwmg.duty(duty)
        utime.sleep_ms(30)
    for duty in range(1023, 0,-30):
        pwmb.duty(duty)
        utime.sleep_ms(50)    

input()
# p2 = Pin(2, Pin.IN)     # create input pin on GPIO2
# print(p2.value())       # get value, 0 or 1
# 
# p4 = Pin(4, Pin.IN, Pin.PULL_UP) # enable internal pull-up resistor
# p5 = Pin(5, Pin.OUT, value=1) # set pin high on creation