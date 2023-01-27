# hw07 - One Wire

## 1-wire temperature sensors

Part 1: P9_12 

Wire all 3 MAX31820 sensors in parallel, with the 1-wire pin being P9_12.

Edit the line in /boot/uEnv.txt to have:
uboot_overlay_addr4=/lib/firmware/BB-W1-P9.12-00A0.dtbo

Reboot

Change to ECE434/hw07

Run tempP9.sh

You will see the 3 temperatures in millidegrees C

Part 2: 

Switch the 1-wire pin to P9_14

Edit the line in /boot/uEnv.txt to have:
uboot_overlay_addr4=/lib/firmware/BB-W1-P9.14-00A0.dtbo

Reboot

Run tempP9.sh

Change to ECE434/hw07

You will see the 3 temperatures in millidegrees C
