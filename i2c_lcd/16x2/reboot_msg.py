#!/usr/bin/python
# Original code found at:
# https://github.com/zzeromin/raspberrypi/tree/master/i2c_lcd
# requires I2C_LCD_driver.py

import I2C_LCD_driver
from time import *
import os

mylcd = I2C_LCD_driver.lcd()
mylcd.lcd_clear()

mylcd.lcd_display_string("rebooting system", 1)
mylcd.lcd_display_string("www.rasplay.org", 2)
sleep(3) # 3 sec delay

os.system("shutdown now -r")
