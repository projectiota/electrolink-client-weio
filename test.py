from electrolinkClient import Electrolink
import time

el = Electrolink('weio.local', 1883)

t = 0
while True:
    print el.digitalWrite(19, t)
    if (t == 0):
        t = 1
    else:
        t = 0
    time.sleep(0.3)

