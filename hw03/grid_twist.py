#!/usr/bin/env python3

#File name: grid_twist.py
#Author: Gaven Williams
#Etch-a-sketch using led matrix, control with 2 encoders

import smbus
import time
import gpiod

getoffsets=[28]
chip = gpiod.Chip('1')
getlines = chip.get_lines(getoffsets)
getlines.request(consumer='getset', type=gpiod.LINE_REQ_EV_BOTH_EDGES)

eQEP1 = '2'
COUNTERPATH1 = '/dev/bone/counter/'+eQEP1+'/count0'

eQEP2 = '1'
COUNTERPATH2 = '/dev/bone/counter/'+eQEP2+'/count0'

ms = 100 # Time between samples in ms
maxCount = '400'
# Set the eEQP maximum count
f = open(COUNTERPATH1+'/ceiling', 'w')
f.write(maxCount)
f.close()

f2 = open(COUNTERPATH2+'/ceiling', 'w')
f2.write(maxCount)
f2.close()

# Enable
f = open(COUNTERPATH1+'/enable', 'w')
f.write('1')
f.close()
f = open(COUNTERPATH1+'/count', 'r')
olddata = -1
bus = smbus.SMBus(1)  # Use i2c bus 1
matrix = 0x70         # Use address 0x70


# Enable
f2 = open(COUNTERPATH2+'/enable', 'w')
f2.write('1')
f2.close()
f2 = open(COUNTERPATH2+'/count', 'r')
olddata2 = -1

delay = 1; # Delay between images in s

bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)



width = 8
height = 8

xpos = 0
ypos = 0

i = 0
j = 0
T = []
#create an array using input dimensions
while i < int(height):
    T.append([])
    while j < int(width):
        T[i].append(" ")
        j += 1
    j = 0
    i += 1

olddata1 = 0
olddata2 = 0

#Game loop. Update after every keyboard input
while True:

    ev_lines = getlines.event_wait()
    if ev_lines:
        for line in ev_lines:
            event = line.event_read()
    vals = getlines.get_values()


    f.seek(0)
    data = f.read()[:-1]
    # Print only if data changes
    print("data = " + data)

    f2.seek(0)
    data2 = f2.read()[:-1]
    print("data2 = " + data2)

    data = int(data)
    data2 = int(data2)


    # #Given input, update x and y positions
    if data > olddata1:
        if ypos <= 0:
            ypos = 0
        else: 
            ypos = ypos - 1

    elif data2 > olddata2:
        if xpos <=0:
            xpos = 0
        else:  
            xpos = xpos - 1

    elif data < olddata1:
        if ypos >= int(height) - 1:
            ypos = int(height) - 1
        else:
            ypos = ypos + 1;

    elif data2 < olddata2:
        if xpos >= int(width) - 1:
            xpos = int(width) - 1
        else:
            xpos = xpos + 1;

    olddata1 = data
    olddata2 = data2

    if vals[0] == 0:
        i = 0
        j = 0
        T = []
        while i < int(height):
            T.append([])
            while j < int(width):
                T[i].append(" ")
                j += 1
            j = 0
            i += 1

        leds = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
        ]
        

    #Update current position from " " to "x"
    T[ypos][xpos] = "x"

    green_bytes = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
    i = 0
    j = 0
    k = 0
    q = 0
    while i < 8:
    
        while j < 8:
            if T[i][j] == "x":
                green_bytes[i] += (0x01 << j)
            j += 1
        j = 0
        i += 1 

    leds = [green_bytes[0], 0x00, green_bytes[1], 0x00, green_bytes[2], 0x00, green_bytes[3], 0x00,
    green_bytes[4], 0x00, green_bytes[5], 0x00, green_bytes[6], 0x00, green_bytes[7], 0x00
    ]

    #Print current x and y positions
    print("x is at: " + str(xpos))
    print("y is at: " + str(ypos))

    # #Print first line (contains x direction lables)
    # line1 = "   "
    # i = 0
    # while i < int(width):
    #     if i < 10:
    #         line1 += ("  " + str(i))
    #     else:
    #         line1 += (" " + str(i))
    #     i += 1
    # print(line1)

    # i = 0
    # j = 0
    # #Print remaining lines, including all lines with "x"s
    # while j < int(height):
    #     if j < 10:
    #         nextline = (str(j) + ": ")
    #     else:
    #         nextline = (str(j) + ":")
    #     while i < int(width):
    #         nextline += "  " + T[j][i]
    #         i += 1
    #     i = 0
    #     print(nextline)
    #     j += 1

    bus.write_i2c_block_data(matrix, 0, leds)
    time.sleep(ms/1000)



