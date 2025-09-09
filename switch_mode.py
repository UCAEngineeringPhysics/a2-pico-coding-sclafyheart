from machine import Pin, PWM, Timer
from time import sleep

# SETUP
dimmer = PWM(Pin(15))
dimmer.freq(1000)

#led = Pin(15, Pin.OUT)
button = Pin(2, Pin.IN, Pin.PULL_DOWN)

def light_up(pin):
    dimmer.duty_u16(65536)

prev = 0
state = False

def toggle_state(pin):
    global state
    state = not state
    
button.irq(trigger=Pin.IRQ_FALLING, handler=toggle_state)

# LOOP

while True:
    if state:
        #Ramp up in 2 seconds
        
        duty = 0
        while duty <= 65536 and state:
            dimmer.duty_u16(duty)
            sleep(2 / 256)
            duty += 256
                
        #Ramp down in 2 second
            
        duty = 65536
        while duty >= 0 and state:
            dimmer.duty_u16(duty)
            sleep(2 / 256)
            duty -= 256
            
    else:
        dimmer.duty_u16(65536)  # Turn off LED when not fading
        sleep(0.1)


        
            
        

