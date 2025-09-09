from machine import Pin, PWM, Timer
from time import sleep

# SETUP
dimmer = PWM(Pin(15))
dimmer.freq(1000)

# LOOP
while True:
    #Ramp up in 2 seconds
    for duty in range(0, 65536, 256):
        dimmer.duty_u16(duty)
        sleep(2 / 256)
        
    #Ramp down in 1 second
    for duty in range(65535, 0, -256):
        dimmer.duty_u16(duty)
        sleep(1 / 256)
