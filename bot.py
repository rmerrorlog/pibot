#!/usr/bin/env python
#-*- coding: utf-8 -*-    #polskie znaki
import time
import os

#MCP3008  # odczyt values[i] = mcp.read_adc(i)
import Adafruit_MCP3008 #numeracja elektryczna
CLK  = 2 
MISO = 3 
MOSI = 4 
CS   = 17 
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

#GPIO
import RPi.GPIO as GPIO
GPIO.setwarnings(False)  # do ogarnięcia

#H-bridhe  l293D #numeracja fizyczna #zapis GPIO.output(3,GPIO.LOW) #(GPIO.input(2)==HIGH odczyt?
HbridgeA = [20,21]
HbridgeB = [19,26]
GPIO.setup(HbridgeA[0],GPIO.OUT)
GPIO.setup(HbridgeA[1],GPIO.OUT)
GPIO.setup(HbridgeB[0],GPIO.OUT)
GPIO.setup(HbridgeB[1],GPIO.OUT)

def Hbridge (id,kierunek):
    if id == "A":
#        print id  " "  kierunek
        GPIO.output(HbridgeA[0],GPIO.LOW)
        GPIO.output(HbridgeA[1],GPIO.LOW)
        if kierunek == 1:
             GPIO.output(HbridgeA[0],GPIO.HIGH)
        if kierunek == 2: 
             GPIO.output(HbridgeA[1],GPIO.HIGH)
    if id == "B":
        GPIO.output(HbridgeB[0],GPIO.LOW)
        GPIO.output(HbridgeB[1],GPIO.LOW)
        if kierunek == 1:
             GPIO.output(HbridgeB[0],GPIO.HIGH)
        if kierunek == 2: 
             GPIO.output(HbridgeB[1],GPIO.HIGH)


#główna pętla
while True:
    values = [0]*8
    for i in range(8):
        values[i] = mcp.read_adc(i)
    print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values))

    if mcp.read_adc(1) > 500:
        Hbridge ("A",1)
        Hbridge ("B",1)
    if mcp.read_adc(1) < 500:
        Hbridge ("A",2)
        Hbridge ("B",2)
                

        
    time.sleep(0.5)
