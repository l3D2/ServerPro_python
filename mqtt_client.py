import paho.mqtt.client as mqtt
import time

class MQTTClient:
    def __init__(self, host, uname, password, port=1883):
        self.host = host
        self.port = port
        self.username = uname
        self.password = password
        self.isConnected = False

        self.client = mqtt.Client(clean_session=True)
        self.client.on_message = self.on_message 
        self.client.on_connect = self.on_connect
        self.client.on_subscribe = self.on_subscribe
        self.client.on_disconnect = self.on_disconnect
        self.client.username_pw_set(self.username, self.password)

    def on_message(self, client, userdata, message):
        raw_message = str(message.payload.decode("utf-8"))
        topic = message.topic
        print(int(time.time()), 'Received', topic, raw_message)

    def on_subscribe(self, client, obj, mid, granted_qos):
        print("Subscribe Succeed")

    def on_connect(self, client, userdata, flags, rc):
        if not self.isConnected:
            if rc == 0:
                print("Connected successfully.")
                self.isConnected = True
            else:
                print("Connection failed with code:", rc)

    def on_disconnect(self, client, userdata, rc):
        if rc != 0:
            print("Unexpected disconnection.")

    def run_mqtt(self):
        self.client.connect(self.host, self.port)
        self.client.subscribe("test/topic")
        self.client.loop_forever()

mqtt_server = MQTTClient("210.246.215.173", "server", "admin")
mqtt_server.run_mqtt()
