#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <signal.h>

#define GPIO0_START_ADDR 0x44E07000
#define GPIO0_END_ADDR 0x44E09000
#define GPIO0_SIZE (GPIO0_END_ADDR - GPIO0_START_ADDR)
#define GPIO1_START_ADDR 0x4804C000
#define GPIO1_END_ADDR 0x4804E000
#define GPIO1_SIZE (GPIO1_END_ADDR - GPIO1_START_ADDR)

#define GPIO_OE 0x134
#define GPIO_DATAIN 0x138
#define GPIO_SETDATAOUT 0x194
#define GPIO_CLEARDATAOUT 0x190
#define GPIO_DATAIN 0x138

// Switches
#define GPIO1_28 (1 << 28)
#define GPIO0_3 (1 << 3)
// LEDS
#define GPIO1_16 (1 << 16)
#define GPIO1_18 (1 << 18)
int running = 1; // Keep the process clean
void signal_handler(int sig);
void signal_handler(int sig)
{
    printf("\nProgram requested to terminate, will exit...\n");
    running = 0;
}

int main(int argc, char *argv[])
{
    volatile void *gpio0_addr;
    volatile unsigned int *gpio0_setdataout_addr;
    volatile unsigned int *gpio0_cleardataout_addr;
    volatile unsigned int *gpio0_oe_addr;
    volatile unsigned int *gpio0_datain_addr;
    volatile void *gpio1_addr;
    volatile unsigned int *gpio1_setdataout_addr;
    volatile unsigned int *gpio1_cleardataout_addr;
    volatile unsigned int *gpio1_oe_addr;
    volatile unsigned int *gpio1_datain_addr;
    unsigned int reg0;
    unsigned int reg1;
    signal(SIGINT, signal_handler);
    int fd = open("/dev/mem", O_RDWR);
    printf("Mapping %X - %X (size %X)\n", GPIO0_START_ADDR, GPIO0_END_ADDR, GPIO0_SIZE);

    gpio0_addr = mmap(0, GPIO0_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO0_START_ADDR);
    gpio0_oe_addr = gpio0_addr + GPIO_OE;
    gpio0_setdataout_addr = gpio0_addr + GPIO_SETDATAOUT;
    gpio0_cleardataout_addr = gpio0_addr + GPIO_CLEARDATAOUT;
    gpio0_datain_addr = gpio0_addr + GPIO_DATAIN;
    if (gpio0_addr == MAP_FAILED)
    {
        printf("Unable to map to GPIO0\n");
        exit(1);
    }
    printf("GPIO mapped to %p\n", gpio0_addr);
    printf("GPIO OE mapped to %p\n", gpio0_oe_addr);
    printf("GPIO SETDATAOUT mapped to %p\n", gpio0_setdataout_addr);
    printf("GPIO CLEARDATAOUT mapped to %p\n", gpio0_cleardataout_addr);

    printf("Mapping %X - %X (size %X)\n", GPIO1_START_ADDR, GPIO1_END_ADDR, GPIO1_SIZE);

    gpio1_addr = mmap(0, GPIO1_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO1_START_ADDR);
    gpio1_oe_addr = gpio1_addr + GPIO_OE;
    gpio1_setdataout_addr = gpio1_addr + GPIO_SETDATAOUT;
    gpio1_cleardataout_addr = gpio1_addr + GPIO_CLEARDATAOUT;
    gpio1_datain_addr = gpio1_addr + GPIO_DATAIN;
    if (gpio1_addr == MAP_FAILED)
    {
        printf("Unable to map to GPIO1\n");
        exit(1);
    }
    printf("GPIO mapped to %p\n", gpio1_addr);
    printf("GPIO OE mapped to %p\n", gpio1_oe_addr);
    printf("GPIO SETDATAOUT mapped to %p\n", gpio1_setdataout_addr);
    printf("GPIO CLEARDATAOUT mapped to %p\n", gpio1_cleardataout_addr);

    reg1 = *gpio1_oe_addr;
    printf("GPIO1 configuration: %X\n", reg1);
    reg1 &= ~GPIO1_16;
    printf("GPIO1 configuration: %X\n", reg1);
    *gpio1_oe_addr = reg1;

    reg1 = *gpio1_oe_addr;
    printf("GPIO1 configuration: %X\n", reg1);
    reg1 &= ~GPIO1_18;
    printf("GPIO1 configuration: %X\n", reg1);
    *gpio1_oe_addr = reg1;

    while (running)
    {
        *gpio1_setdataout_addr = GPIO1_16;
        //usleep(250000);
        *gpio1_cleardataout_addr = GPIO1_16;
        //usleep(250000);
    }
    munmap((void *)gpio0_addr, GPIO0_SIZE);
    munmap((void *)gpio1_addr, GPIO1_SIZE);
    close(fd);
    return 0;
}
