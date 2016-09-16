from electrolinkClient import Electrolink
import time

el = Electrolink('weio.local', 1883)

t = 0
while True:
    # print "fade in" in the console
    print "fade in"
    # count from 0 to 100 % 
    for i in range(0,100):
        # change PWM duty cycle to i
        el.pwmWrite(20,i)

    # print "fade out" in the console
    print "fade out"  
    # count from 0 to 100 % 
    for i in range(0,100):
        # change PWM duty cycle to 100-i
        el.pwmWrite(20,100-i)

