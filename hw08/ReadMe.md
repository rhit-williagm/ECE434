# hw08 - PRU

## Blinking an LED
What command will start the PRU?
echo "start" > /sys/class/remoteproc/remoteproc1/state

What command will stop it?
echo "stop" > /sys/class/remoteproc/remoteproc1/state

With blink.pru0.c, the PRU toggles P9_31. 

Make sure that P9_31 is configured to gpio, with direction set to out in /sys/class/gpio/gpio110

## PWM Generator

The file pwm1.pru0.c toggles pin P9_31 at 50 MHz

pwm1.jpg shows the waveform. It isn't very square, which is probably due to the breadboard at such a high frequency. There isn't much jitter though. 

## Controlling the PWM Frequency

What output pins are being driven?
P9_28, P9_29, P9_30, P9_31

pwm4.jpg shows all 4 pwm channels on one scope capture. 

## Reading an Input at Regular Intervals

