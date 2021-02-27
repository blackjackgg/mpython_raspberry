import time
from umqtt.simple import MQTTClient

# Publish test messages e.g. with:
# mosquitto_pub -t foo_topic -m hello
def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('duote', '77777777')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
# Received messages from subscriptions will be delivered to this callback
do_connect()
def sub_cb(topic, msg):
    print((topic, msg))

def main(server="mqtt.bconimg.com"):
    c = MQTTClient("umqtt_client", server)
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(b"beacon")
    while True:
        if True:
            # Blocking wait for message
            c.wait_msg()
        else:
            # Non-blocking wait for message
            c.check_msg()
            # Then need to sleep to avoid 100% CPU usage (in a real
            # app other useful actions would be performed instead)
            time.sleep(1)

    c.disconnect()

main()