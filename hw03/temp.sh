#!/usr/bin/env bash
TEMP=$(i2cget -y 1 0x48)
TEMP2=$((16#${TEMP:2}))
TEMP3=$(((($TEMP2*9)/5)+32))
echo $TEMP3