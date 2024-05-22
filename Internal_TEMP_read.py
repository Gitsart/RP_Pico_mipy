#pico has an inbuilt Temperature sensor
#this feature is connected to ADC4
#we will read the temperature using the ADC4
#for 27 degree Celcius, voltage is 0.706V
#for every degree rise, voltage drops by 1.721mV

from machine import ADC

temp_sen = ADC(4)

def read_temp():
    #function to read ADC value
    adc_val = temp_sen.read_u16()
    
    #converting ADC value to voltage
    voltage = adc_val * (3.3/65535.0)
    
    #use formula for temp calculation
    temperature = 27 - (voltage -0.706)/0.001721
    
    return temperature


#read & print the internal temperature
tempC = read_temp()

print("Inside temperature:", tempC, "C")
