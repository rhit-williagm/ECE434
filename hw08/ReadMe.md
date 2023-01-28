# hw08 - PRU

## Blinking an LED
What command will start the PRU?
echo "start" > /sys/class/remoteproc/remoteproc1/state

What command will stop it?
echo "stop" > /sys/class/remoteproc/remoteproc1/state

USR3 works, header pins do not. 

## PWM Generator

## Controlling the PWM Frequency

What output pins are being driven?
P9_28, P9_29, P9_30, P9_31

## Reading an Input at Regular Intervals

get a transistor so that you don't fry your beaglebone
