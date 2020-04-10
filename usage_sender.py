# -*- coding: utf-8 -*-
import psutil
import time
import paho.mqtt.client as mqtt
import json

client = mqtt.Client()
client.connect("127.0.0.1", 1883, 60) #host, port, keepalive

while True:
    cpu = psutil.cpu_percent(interval=None)
    print('CPU usage: '+ str(cpu) + '%')

    mem = psutil.virtual_memory().percent
    print('Memory usage: ' + str(mem) + '%')

    disk = psutil.disk_usage('/').percent
    print('Disk usage: ' + str(disk) + '%')

    temp = psutil.sensors_temperatures()['cpu-thermal'][0].current
    print('Temperature: ' + str(temp) + '°C')

    print('-----------------------------')

    send_msg = {'cpu': cpu, 'mem': mem, 'disk': disk, 'temp': temp}

    client.publish('smartHome/usage', payload=json.dump(send_msg), qos=2, retain=False)
    time.sleep(.500)