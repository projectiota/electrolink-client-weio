## Electrolink Client for WeIO
Example of using [electrolink-client-mqtt-python](https://github.com/projectiota/electrolink-client-mqtt-python) library
to drive WeIO board remotely.

## Usage

- Start [electrolinkServer](https://github.com/nodesign/weio/blob/next/examples/webService/electrolinkServer/main.py) on
WeIO board

- Make sure that MQTT broker (Mosquitto) is running on WeIO board as described
[here](https://github.com/nodesign/weio/wiki/MQTT#mqtt-broker---mosquitto), otherwise use some other server
[here](https://github.com/projectiota/electrolink-client-weio/blob/94e076e4397b954b375e01217fd70ab6dd4cdba5/test.py#L4)

- Execute the test on PC:
```bash
python test.py
```
> N.B. Once started, test can be stopped from another terminal by executing:
> `ps aux | grep python | grep test | awk '{print $2}' | xargs kill`

## License
[Apache-2.0](LICENSE)
