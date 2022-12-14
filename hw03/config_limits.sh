#!/usr/bin/env bash

# Filename: config_limits.sh
# Author: Gaven Williams
# Configures TMP101 THIGH and TLOW

config-pin P9_11 gpio
config-pin P9_13 gpio
config-pin P9_17 i2c
config-pin P9_18 i2c
i2cset -y 1 0x48 0x02 0x15
i2cset -y 1 0x48 0x03 0x1b
i2cset -y 1 0x4a 0x02 0x15
i2cset -y 1 0x4a 0x03 0x1b
echo done