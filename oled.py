# 中文啦
from machine import I2C,Pin, SoftI2C
# Create the I2C interface.
i2c = I2C(0,scl=Pin(18), sda=Pin(19), freq=400000)
i2c.scan()
# i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)
# i2c.scan()
print(i2c.scan())

from ssd1306 import SSD1306_I2C
oled = SSD1306_I2C(128, 64, i2c)
# oled.fill(1)
# oled.show()
# oled.pixel(0, 0, 1)
# oled.show()
# oled.pixel(127, 63, 1)
# oled.show()
# oled.text('zhang', 0, 0)
# oled.text('man#', 0, 20)
# oled.text('ip:192.168.1.1', 0, 30)
oled.chinese('我爱张曼', 2, 2)  # 中文按行来 
oled.show()
# 
# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
# display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
# # Alternatively you can change the I2C address of the device with an addr parameter:
# #display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x31)
# 
# # Clear the display.  Always call show after changing pixels to make the display
# # update visible!
# display.fill(0)
# print(i2c.readfrom(8, 4))
# i2c.writeto(0x3a, '15') # write '12' to device with address 0x3a
# buf = bytearray(10)     # create a buffer with 10 bytes
# i2c.writeto(0x3a, buf)  # write the given buffer to the slave
# print(i2c.readfrom(0x3a, 4))