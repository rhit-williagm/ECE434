# HW04 - MMAP and LCD
## Memory Map
              
| Block Name | Start Address | End Address | Size | Description |
|------|---------------|-------------|------|-------------|
| EMIF0 SDRAM | 0x8000_0000 | 0xBFFF_FFFF | 1 GB | 8-/16-bit External Memory |
| GPIO0 | 0x44E0_7000 | 0x44E0_7FFF | 4KB | GPIO0 Registers |
| GPIO0 | 0x44E0_8000 | 0x44E0_8FFF | 4KB | Reserved |
| GPIO1 | 0x4804_C000 | 0x4804_CFFF | 4KB | GPIO1 Registers |
| GPIO1 | 0x4804_D000 | 0x4804_DFFF | 4KB | Reserved |
| GPIO2 | 0x481A_C000 | 0x481A_CFFF | 4KB | GPIO2 Registers |
| GPIO2 | 0x481A_D000 | 0x481A_DFFF | 4KB | Reserved |
| GPIO3 | 0x481A_E000 | 0x481A_EFFF | 4KB | GPIO3 Registers |
| GPIO3 | 0x481A_F000 | 0x481A_FFFF | 4KB | Reserved |

## GPIO via mmap
Execute ./switchled to toggle 2 leds with P9_12 and P9_21 with mmap
Execute ./toggleled to toggle an led with mmap

With delay, the led toggled at ~2 Hz
Without delay, it toggled ~2.94 MHz

## I2C via the kernel driver
Run ./temp.sh to read the value of TMP101 in millidegrees C using the kernel

## LED matrix etch-a-sketch using Flask
Run ./sketch.py to start the game. Contol at 192.168.7.2:8081, using the UP, DOWN, LEFT, and RIGHT options

## LCD Display

Can display images and movies

Run ./image.sh to see a sideways-flipped boris
Run ./movie.sh to play a short movie

# hw04 grading

| Points      | Description | |
| ----------- | ----------- | - |
|  2/2 | Memory map 
|  4/4 | mmap()
|  4/4 | i2c via Kernel
|  5/5 | Etch-a-Sketch via flask
|  5/5 | LCD display
|      | Extras
| 20/20 | **Total**
*Looks good.*
*My comments are in italics. --may*

