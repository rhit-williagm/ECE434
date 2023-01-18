# hw06
## "What Every Driver Developer Should Know about RT"
1. Where does Julia Cartwright work?

National Instruments

2. What is PREEMT_RT? Hint: Google it.

Allows interrupts to run as threads, which gives the ability to modify the priorities of interrupts. 

3. What is mixed criticality?

System that has multiple types of tasks, such as real-time requirements mixed with non-timed tasks. Mixed criticality refers to two degree of time-sensitiveness. 

4. How can drivers misbehave?

The driver stacks are shared between both RT and non-RT processes, which can cause the drivers to misbehave. 

5. What is Δ in Figure 1?

Tevent – Tapplication, which is the time between some event occurring and a real-time task actually executing

6. What is Cyclictest?
Take a time stamp, sleep for a fixed duration, take another time stamp when the thread is woken up. The difference between these time stamps (minus the sleep duration) 
is Δ. 

7. What is plotted in Figure 2?

Distribution of latency samples, showing both preempt and preempt_rt. 

8. What is dispatch latency? Scheduling latency?

Dispatch latency is the time between the hardware event firing and the relevant thread to be woken up. 
Scheduling latency is the time between the scheduler being aware of the task and the CPU being given the task to run. 

9. What is mainline?

All events have same priority, interrupts happen in the order they are received. Certain events don’t have priority over others. 

10. What is keeping the External event in Figure 3 from starting?

Low priority interrupt is still executing. 

11. Why can the External event in Figure 4 start sooner?

Higher priority interrupt allows it to. 
