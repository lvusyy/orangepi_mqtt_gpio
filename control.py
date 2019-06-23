#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: lvusyy
@license: Apache Licence 
@contact: lvusyy@gmail.com
@site: https://github.com/lvusyy/
@software: PyCharm
@file: control.py
@time: 2018/3/13 17:30
"""
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import threading
import time
from mqttMange import MqttMange
from gpio import GPIO

class Light():

    def __init__(self):
        self.pin=18
        self.mode=1 #open is 1 close is 0
        self.mgpio=GPIO()
        self.mgpio.setPinMode(pin=self.pin,mode=1) #OUTPUT 1 INPUT 0

    def on(self):
        ''
        self.mgpio.setV(self.pin,self.mode)

    def off(self):
        ''
        self.mgpio.setV(self.pin,self.mode&0)

    def status(self):
        #0 is off 1 is on
        return self.mgpio.getV(self.pin)


def checkLightStatus(light):
    ''
    while True:
        for i in range(20):
            time.sleep(60)
        if light.status!=0:
            light.off()

l=Light()
t=threading.Thread(target=checkLightStatus,args=(l,))
t.setDaemon(True)
t.start()


def respStatus():
    statusText="电灯已经关闭" if l.status()==0 else "电灯已经打开"
    mq.client.publish('t1/light1',statusText)

def P_mqttMsg(msg):
    ''
    plant={'on':l.on,'off':l.off,'status':respStatus}

    for o in plant.keys():
        if o in msg:
            plant[o]()


mq=MqttMange(P_mqttMsg)
#mq.client.publish('t1/light1',"test") #ok
mq.loop()