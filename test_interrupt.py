from electrolinkClient import Electrolink
import time

el = Electrolink('weio.local', 1883)

t = 0

def myCb():
    print "###>>> INERRUPT DETECTED"

##
# LOW = 0
# HIGH = 1
# CHANGE = 2
# RISING = 3
# FALLING = 4
##
el.attachInterrupt(19, 3, myCb)

while True:
    print el.digitalWrite(19, t)
    if (t == 0):
        t = 1
    else:
        t = 0
    time.sleep(3)

