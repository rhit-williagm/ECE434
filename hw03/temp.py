#!/usr/bin/env python3

#File name: temp.py
#Author: Gaven Williams
#Prints temperature values (in F) from 2 TMP101 chips

import smbus
import time

bus = smbus.SMBus(1)
address1 = 0x48
address2 = 0x4a

while True:
    temp1 = bus.read_byte_data(address1, 0)
    temp2 = bus.read_byte_data(address2, 0)
    temp1 = ((temp1*9)/5) + 32
    temp2 = ((temp2*9)/5) + 32
    print("Chip 1 temp: " + str(temp1) + "F")
    print("Chip 2 temp: " + str(temp2) + "F")
    print("\r")
    time.sleep(0.25)