#!/usr/bin/env python
# // This uses the eQEP hardware to read a rotary encoder
# // bone$ config-pin P8_11 eqep
# // bone$ config-pin P8_12 eqep
import time

eQEP1 = '1'
COUNTERPATH1 = '/dev/bone/counter/'+eQEP1+'/count0'

eQEP2 = '2'
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

# Enable
f2 = open(COUNTERPATH2+'/enable', 'w')
f2.write('1')
f2.close()
f2 = open(COUNTERPATH2+'/count', 'r')
olddata2 = -1

while True:
    f.seek(0)
    data = f.read()[:-1]
    f2.seek(0)
    data2 = f2.read()[:-1]
    # Print only if data changes
    if data != olddata:
        olddata = data
        print("data = " + data)
    if data2 != olddata2:
        olddata2 = data2
        print("data2 = " + data2)
    time.sleep(ms/1000)
