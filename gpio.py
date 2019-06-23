#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: lvusyy
@license: Apache Licence 
@contact: lvusyy@gmail.com
@site: https://github.com/lvusyy/
@software: PyCharm
@file: gpio.py
@time: 2018/3/13 18:45
"""
import wiringpi as wp


class GPIO():

    def __init__(self):
        self.wp=wp
        wp.wiringPiSetupGpio()
        #wp.pinMode(18, 1)
        #wp.pinMode(23, 0)

    def setPinMode(self,pin,mode):
        self.wp.pinMode(pin,mode)

    def setV(self,pin,v):
        self.wp.digitalWrite(pin,v)

    def getV(self,pin):
        return self.wp.digitalRead(pin)