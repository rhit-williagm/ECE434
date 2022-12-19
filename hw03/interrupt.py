#!/usr/bin/env python3

import smbus
import time
import gpiod
import sys

#File name: interrupt.py
#Author: Gaven Williams
#Prints temperature values if temp exceeds THIGH or goes below TLOW

getoffsets=[30, 31]
chip = gpiod.Chip('0')
getlines = chip.get_lines(getoffsets)
getlines.request(consumer='getset', type=gpiod.LINE_REQ_EV_FALLING_EDGE)

bus = smbus.SMBus(1)
address1 = 0x48
address2 = 0x4a

config_reg1 = bus.read_byte_data(address1, 1)
bus.write_byte_data(address1, 1, config_reg1 | 2)
config_reg2 = bus.read_byte_data(address2, 1)
bus.write_byte_data(address2, 1, config_reg2 | 2)

while True:
    ev_lines = getlines.event_wait(sec=1)
    if ev_lines:
        for line in ev_lines:
            event = line.event_read()
    vals = getlines.get_values()

    print("vals[0] = " + str(vals[0]))
    print("vals[1] = " + str(vals[1]))
    if vals[0] == 0:
        temp1 = bus.read_byte_data(address1, 0)
        temp1 = ((temp1*9)/5) + 32
        print("Chip 1 temp: " + str(temp1) + "F")

    if vals[1] == 0:
        temp2 = bus.read_byte_data(address2, 0)
        temp2 = ((temp2*9)/5) + 32
        print("Chip 2 temp: " + str(temp2) + "F")

    

    time.sleep(0.25)