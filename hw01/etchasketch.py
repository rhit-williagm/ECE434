#!/usr/bin/env python3

#File name: etchasketch.py
#Author: Gaven Williams
#Date: 12/9/2022

print()
print("Welcome to Gaven's Super Etch-A-Sketch Simulator!")
print("Use WASD to move your cursor. Cear with c. Confirm size input with {ENTER}")
print("Channel your inner artist to create a picture like so:")
print("   0 1 2 3 4 5 6 7")
print("0:     x x x x    ")
print("1:   x         x  ")
print("2: x   x     x   x")
print("3: x             x")
print("4: x   x     x   x")
print("5: x     x x     x")
print("6:   x         x  ")
print("7:     x x x x    ")
width = input("Set grid width:")
height = input("Set grid height:")


if int(width) > 99 or int(height) > 99 or int(width) <= 0 or int(height) <= 0:
    print("Invalid size")
    exit(0)



print("Have fun!")

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

#Game loop. Update after every keyboard input
while True:
    key = input(" ")

    #Given input, update x and y positions
    if key == 'w' or key == 'W':
        if ypos <= 0:
            ypos = 0
        else: 
            ypos = ypos - 1

    elif key == 'a' or key == 'A':
        if xpos <=0:
            xpos = 0
        else:  
            xpos = xpos - 1

    elif key == 's' or key == 'S':
        if ypos >= int(height) - 1:
            ypos = int(height) - 1
        else:
            ypos = ypos + 1;

    elif key == 'd' or key == 'D':
        if xpos >= int(width) - 1:
            xpos = int(width) - 1
        else:
            xpos = xpos + 1;

    elif key == 'c' or key == "C":
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

    #Update current position from " " to "x"
    T[ypos][xpos] = "x"

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



