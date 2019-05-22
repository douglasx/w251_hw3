import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("image_msg")

def on_message(client, userdata, msg):  # The callback for when a PUBLISH message is received from th
    message = msg.payload
    print("Message received-> " + msg.topic + " " + str(msg.payload))  # Print a received msg
    return message


client = mqtt.Client()  # Create instance of client with client ID ...digi_mqtt_test...
client.connect('172.18.0.2', 1883,60)

client.on_connect = on_connect
client.on_message = on_message  # Define callback function for receipt of a message
#client.loop_forever()


#client1 = mqtt.Client()
client.connect('184.173.61.36',1883,60)
client.publish('image_msg_cloud',str(on_message))

client.loop_forever()

