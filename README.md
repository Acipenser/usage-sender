# usage-sender
Sending performance data of a Raspberry PI via MQTT

## Run script
``` nohup python usage-sender.py &> /dev/null &```

## Stop script
```sudo kill $(ps aux | grep '[u]sage-sender.py' | awk '{print $2}')```
