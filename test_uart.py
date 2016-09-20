from electrolinkClient import Electrolink
import time, sys

el = Electrolink('weio.local', 1883)

t = 0
print el.uartStart(115200)
while True:
    print el.uartSend("Hello, world!\r\n")
    res = el.uartReceive()["result"]
    print res
    if res == "quit":
        print el.uartStop()
        sys.exit(0)
    time.sleep(1)

