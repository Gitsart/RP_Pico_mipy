from machine import Pin
from time import sleep
led = Pin(25, Pin.OUT) #Built_in LED pin for pico
while True:
    led.value(0)
    sleep(0.5)
    led.value(1)
    sleep(0.5)