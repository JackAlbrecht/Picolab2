#/importing machine and utime libraries, led variable is PWM (variable power 2^16) on pin 15, the led is sent power every 1ms
#/the brightness range allows us to go from 0-2^16 (0-100%) within a for loop to go through every value between 0-2^16 in increments of 50.
#/the for loop tells us to wait 10ms between each increment instead of computing as fast as possible, and then the duty is set to 0 (off).

import machine
import utime

led = machine.PWM(machine.Pin(12))

#/says how often the variable led cycles through power (off and on)
led.freq(1000)

#/from no brightness (0) to full brightness (2^16), it goes through increments of 50
for brightness in range(0,65535,50):
    #/ for loop goes through brightness on led from 0%-100% in increments of 50.
    led.duty_u16(brightness)
    #/waits 10ms to get brighter.
    utime.sleep_ms(10)
#/ lights are at 0% brightness
led.duty_u16(0)
