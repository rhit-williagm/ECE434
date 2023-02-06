# hw09 - Logging data in the cloud

## MAX31820 Temperature Sensors

Make sure you have the following line in /boot/uEnv.txt:

uboot_overlay_addr4=/lib/firmware/BB-W1-P9.14-00A0.dtbo

With local_temp.py, you can read the 3 temperature sensors in degrees F

## Logging in Sheets

With tempio.py, you can log this temperature data to a Google sheet, which timestamps the values, updating every 5 seconds. 

https://docs.google.com/spreadsheets/d/11kXlemcXhCeBH2b27nGgpiMxc4ouMmpqc6sb9AFcaZM/edit#gid=0
