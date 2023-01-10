#!/usr/bin/env python3
# From: https://towardsdatascience.com/python-webserver-with-flask-and-raspberry-pi-398423cc6f5d
# Author: Gaven Williams
# Etch - a - sketch controlled with Flask
# 1/9/2023
import gpiod
import sys
import smbus
import time
# import Adafruit_BBIO.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)
bus = smbus.SMBus(2)  # Use i2c bus 1
matrix = 0x70         # Use address 0x70
delay = 1; # Delay between images in s
bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)


#Set all variables
width = 0
height = 0
xpos = 0
ypos = 0
i = 0
j = 0
T = 0
green_bytes = 0
k = 0
q = 0
leds = 0
line1 = 0

width = 8
height = 8

xpos = 0
ypos = 0

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

#Main html page
@app.route("/")
def index():
    global width 
    global height
    global xpos 
    global ypos 
    global i 
    global j 
    global T 
    global green_bytes
    global k 
    global q 
    global leds 
    global line1 
    return render_template('index4.html')

#Action pages
@app.route("/<action>")
def action(action):
    global width 
    global height
    global xpos 
    global ypos 
    global i 
    global j 
    global T 
    global green_bytes
    global k 
    global q 
    global leds 
    global line1
    if action == "up":
        if ypos <= 0:
            ypos = 0
        else: 
            ypos = ypos - 1
    if action == "down":
        if ypos >= int(height) - 1:
            ypos = int(height) - 1
        else:
            ypos = ypos + 1;
		
    if action == "left":
        if xpos <=0:
            xpos = 0
        else:  
            xpos = xpos - 1

    if action == "right":
        if xpos >= int(width) - 1:
            xpos = int(width) - 1
        else:
            xpos = xpos + 1;

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

    #Print first line (contains x direction lables)
    line1 = "   "
    i = 0
    while i < int(width):
        if i < 10:
            line1 += ("  " + str(i))
        else:
            line1 += (" " + str(i))
        i += 1
    print(line1)

    i = 0
    j = 0
    #Print remaining lines, including all lines with "x"s
    while j < int(height):
        if j < 10:
            nextline = (str(j) + ": ")
        else:
            nextline = (str(j) + ":")
        while i < int(width):
            nextline += "  " + T[j][i]
            i += 1
        i = 0
        print(nextline)
        j += 1

    bus.write_i2c_block_data(matrix, 0, leds)
    return render_template('index4.html')


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8081, debug=True)