# hw05
## Make
bone$ gcc -g -c app.c -o app.o
In the above command:
Target: app.o
Dependency: app.c
Command: gcc

The -c option in the above gcc command tells gcc to compile the following file, app.c in this case

My Makefile is included in this repo

## Kernel Modules
gpio_test1.c allows the user to toggle an LED on P9_16 with P9_15

gpio_test2.c allows the above, plus an additional LED on P9_17 with P9_18
