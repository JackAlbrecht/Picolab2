#/This program uses the machine and utime libraries to match pin 14 to button input, then allowing us to measure when button is pressed
#/which is value 1. If value is 1 then it will say the print phrase in the shell, then utime.sleep allows it to have a cooldown for how often
#/you can measure a button value as 1.

import machine
import utime

button = machine.Pin(11, machine.Pin.IN)
while True:
    #/this says if the button is in on position(1) then do the below
    if button.value() == 1: 
    #/shows the quotations in the shell
        print("You pressed the button!")
    #/resets after .25 seconds (you wont get a response until after this time)
        utime.sleep(.25)
