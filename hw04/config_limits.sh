#!/usr/bin/env bash

# Filename: config_limits.sh
# Author: Gaven Williams
# Configures TMP101 THIGH and TLOW

config-pin P9_11 gpio
config-pin P9_13 gpio
config-pin P9_19 i2c
config-pin P9_20 i2c
echo done