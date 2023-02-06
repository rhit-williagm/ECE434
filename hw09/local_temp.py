#!/usr/bin/env python3

tmpPATH="/sys/class/hwmon/"

fd = open(tmpPATH + "hwmon0/temp1_input")
temp1 = float(fd.read().replace('\n', ''))/1000
temp1 = 9/5*temp1 + 32
fd.close()

print(temp1)

fd = open(tmpPATH + "hwmon1/temp1_input")
temp2 = float(fd.read().replace('\n', ''))/1000
temp2 = 9/5*temp2 + 32
fd.close()

print(temp2)

fd = open(tmpPATH + "hwmon2/temp1_input")
temp3 = float(fd.read().replace('\n', ''))/1000
temp3 = 9/5*temp3 + 32
fd.close()

print(temp3)