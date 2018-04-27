# Raspberry Pi IoT Experience
this only works on a raspberry pi. all you need is a raspberry pi.
The script measures the temperature on the pi, then uploads it to a Thingspeak channel.

# Instructions

## Create a Thingspeak account
Follow the instructions here: https://www.dexterindustries.com/BrickPi/brickpi-tutorials-documentation/projects/thingspeak-temperature-log/

**Step1 to Step7 only.**

## Clone this repo
```bash
git clone https://github.com/yuk0ga/Temp-uploader.git
```

## Add API key
Reveiw Step 6 from the instruction above.

## Run
Then ignore the steps after Step7, and run the python script
```bash
sudo python Thermometer_Thingspeak.py
```
Go to your channel on Thingspeak, and you'll see the graph plotted
