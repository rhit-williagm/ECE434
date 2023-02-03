#include <stdint.h>
#include <pru_cfg.h>
#include "resource_table_empty.h"
#include "prugpio.h"

volatile register unsigned int __R30;
volatile register unsigned int __R31;

void main(void) {
	int i;

	uint32_t *gpio0 = (uint32_t *)GPIO0;
	
	/* Clear SYSCFG[STANDBY_INIT] to enable OCP master port */
	CT_CFG.SYSCFG_bit.STANDBY_INIT = 0;

	for(i=0; i<10; i++) {
		gpio0[GPIO_SETDATAOUT]   = 1<<30;	// P9_31 LED on

		__delay_cycles(500000000/5);    	// Wait 1/2 second

		gpio0[GPIO_CLEARDATAOUT] = 1<<30;  // P9_31 LED off

		__delay_cycles(500000000/5); 

	}
	__halt();
}

