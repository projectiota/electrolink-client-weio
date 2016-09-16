from electrolinkClient import Electrolink
import time

el = Electrolink('weio.local', 1883)

t = 0
while True:
    print el.analogRead(31)
    time.sleep(0.3)

