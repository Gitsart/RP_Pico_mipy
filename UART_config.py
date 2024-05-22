##pico has 2UARTs:UART0 which can be mapped to GPIO0/1&12/13
##and UART1 mapped to 4/5 and 8/9

from machine import UART, Pin
uart1 = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))
uart1.write('hello') #5byte writing
uart1.read(5)        #read upto 5 bytes.

uart1.read(10)  #read 10 bytes
uart1.read()    #read all available characters
