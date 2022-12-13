#!/usr/bin/env python3
# //////////////////////////////////////
# 	toggle1.py
#  Toggles the P9_21 pin as fast as it can. P9_21 is line 3 on chip 0.
# 	Wiring:	Attach an oscilloscope to P9_21 to see the squarewave or 
#          uncomment the uleep and attach an LED.
# 	Setup:	sudo apt update; pip install gpiod
# 	See:	https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/tree/bindings/python/examples
# //////////////////////////////////////

import gpiod
import time

LED_CHIP = 'gpiochip0'
LED_LINE_OFFSET = [3]  # P9_21, run: gpioinfo | grep -i -e chip -e P9_21

chip = gpiod.Chip(LED_CHIP)

lines = chip.get_lines(LED_LINE_OFFSET)
lines.request(consumer='toggle1.py', type=gpiod.LINE_REQ_DIR_OUT)

while True:
    lines.set_values([0])
    lines.set_values([1])
    