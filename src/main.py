import paho.mqtt.client as mqttClient
import time
import json
from connection import Connection


connected = False

def on_connect(client, userdata, flags, rc):

    if rc == 0:

        print("Connected to broker")

        global connected
        connected = True

    else:

        print("Connection failed")


def client_setup(conn, client):
    client.username_pw_set(conn.user, password=conn.password)
    client.on_connect = on_connect
    client.connect(conn.broker_address, port=conn.port)



def main():
    c = Connection("127.0.0.1", 1883, "lucas", "senha")

    client = mqttClient.Client("lucas")
    client_setup(c, client)


    client.loop_start()

    while connected != True:
        time.sleep(0.1)

    with open('test.txt') as f:
        json_data = json.load(f)

    client.publish("MapaDCC",str(json_data))


    client.disconnect()
    client.loop_stop()


if __name__ == '__main__':
    main()
