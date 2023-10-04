import machine
import utime

#/red, green, and blue are the corresponding pins for power, labeled as PWM for changes in levels of power.
red = machine.PWM(machine.Pin(13))
green = machine.PWM(machine.Pin(14))
blue = machine.PWM(machine.Pin(15))
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

color_set(0,50,255)
