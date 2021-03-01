from machine import Pin,PWM
import utime

 
servo=Pin(18, Pin.OUT) #port 2 is used for led
pwmr = PWM(servo)
pwmr.freq(500)



while True:
    for duty in range(0,1023, 80):
        pwmr.duty(duty)
        utime.sleep_ms(60)