#hw02 - GPIO
##Measuring GPIO pin on an oscilloscope
1. Min voltage: -222.4 mV Max voltage: 3.20 V
2. Period: 122.275 ms Frequency: 8.18 Hz
3. How close to 100ms? 22.275 ms slower
4. Why do they differ? Overhead/latency from running the script; other programs are also running at the same time, so the CPU usage isn’t solely dedicated to this program. 
5. % usage of CPU: 4%
6. Table of sleep time results:

| Sleep time | Period (ms) | CPU Usage (%) |
|------------|-_-----------|---------------|
|0.1         | 122.3       | 4             |
|0.05        | 71.5        | 5.9           | 
|0.01        | 32.6        | 12.3          |
|0.005       | 25.7        | 14.1          | 
|0.001       | 23.2        | 15.2          |

7. How stable is the period? Very unstable, especially when inputting smaller sleep times (I’m also running VScode)
8. Period stability after launching vi? Period becomes even less stable
9. Remove unneeded lines; does it change the period? Not that I can tell
10. Use .sh. Does the period change? Slightly, now when input is 0.1 ms I get period of ~117 ms
11. Shortest period you could get? Roughly 16 ms

##Table of results; Python vs. C

|            | Python (1 bit) | C (1 bit) | Python (2 bits) | C (2 bits) |
|------------|----------------|-----------|-----------------|------------|
| Period:    | 19.8 us        | 3.89 us   | 20.1 us         | 3.92 us    |
| Frequency: | 50.5 kHz       | 257.1 kHz | 49.8 kHz        | 255.1 kHz  |
| CPU Usage: | 75.4%          | 95.5%     | 77.2%           | 95.7%      |
