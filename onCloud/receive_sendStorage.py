import paho.mqtt.client as mqtt

# This is the Subscriber

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("image_msg_cloud")

def on_message(client, userdata, msg):
#    continue
    if msg.payload.decode() == "Hello world!":
        print("Yes!")
   # client.disconnect()

client = mqtt.Client()
client.connect("184.173.61.36",1883,60)

client.on_connect = on_connect
#client.on_message = on_message

client.loop_forever()

client1.mqtt.Clent()
client1.connect("cos://us-south/01facestoragew251hw3dougxu",1883,60)
client1.publish('image_msg',payload=msg)

