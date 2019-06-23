#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: lvusyy
@license: Apache Licence 
@contact: lvusyy@gmail.com
@site: https://github.com/lvusyy/
@software: PyCharm
@file: MqttMange.py
@time: 2018/3/13 17:39
"""
from control import P_mqttMsg
import paho.mqtt.client as mqtt

class MqttMange(object):

    def __init__(self):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect("118.24.74.159", 1888, 60)

        # Blocking call that processes network traffic, dispatches callbacks and
        # handles reconnecting.
        # Other loop*() functions are available that give a threaded interface and a
        # manual interface.
    def loop(self):
        self.client.loop_forever()

    def on_connect(self,client, userdata, flags, rc):
        print("Connected with result code "+str(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe("t1/light1")

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self,client, userdata, msg):
        print(msg.topic+" "+str(msg.payload)+" Qos "+str(msg.qos))
        P_mqttMsg(msg.payload)

