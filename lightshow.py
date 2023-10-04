#/red, green, and blue are the corresponding pins for power, labeled as PWM for changes in levels of power.
red = machine.PWM(machine.Pin(13))
green = machine.PWM(machine.Pin(14))
blue = machine.PWM(machine.Pin(15))
led = machine.Pin(12, machine.Pin.OUT)
#/sets frequency of electrical current to 1000 (1ms) for all pins with LEDs attached.
red.freq(1000)
green.freq(1000)
blue.freq(1000)
#/matches color values to duty values because duty is 2^16 and colors are 2^8
def interval_mapping(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
def color_to_duty(rgb_value):
    rgb_value = int(interval_mapping(rgb_value,0,255,0,65535))
    return rgb_value

#/ sets color based on 24bit, 8bit per light, allowing us to set values from 0-255 for all lights, as seen below.
def color_set(red_value,green_value,blue_value):
    red.duty_u16(color_to_duty(red_value))
    green.duty_u16(color_to_duty(green_value))
    blue.duty_u16(color_to_duty(blue_value))
    
#/sets information for how long it takes for action to start after button is pushed
#/sets the if elif statement, i found i couldn’t do if else without issues.  
button = machine.Pin(11, machine.Pin.IN)
while True:
    utime.sleep(.2)
    if button.value() == 0:
         color_set(250,250,250)
         led.value(0)
    elif button.value() == 1:
            led.value(1) #turns the led on
            color_set(0,0,0)
