import utime,time,random
import math
from array import array
from machine import Pin,ADC,DAC,PWM

adc = ADC(Pin(33))
a2 = Pin(33)
out = Pin(26)

sound = PWM(out)

def tone(pin,freq, duration=0, duty=30):
    pin.freq(int(freq))
    pin.duty(duty)
    time.sleep_us( int(duration * 0.9 * 1000) )
    pin.duty(0)
    time.sleep_us(int(duration * 0.1 * 1000))

while True:
    freq = random.randint(1000,3000)
    print(freq)
    tone(sound,freq,500)
    ## random music

# try:
#     while 1:
#         t1 = utime.ticks_us()
#         voice = adc.read()
#         print(voice)
# #         dac.write(voice)
# #         sound.duty(voice)
# #         sound.freq(150000)
# except KeyboardInterrupt:
#     pass