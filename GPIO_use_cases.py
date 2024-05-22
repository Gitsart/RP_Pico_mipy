from machine import Pin

p0 = Pin(0, Pin.OUT)  #set GPIO pin0 as output
p0.on()  #p0.value(1) #set pin0 as HIGH
p0.off()              #set pin0 LOW

p2 = Pin(2, Pin.IN)    #create input at pin2

p3 = Pin(4, Pin.IN, Pin.PULL_UP)  #input pullup condition at pin3

