#!/bin/sh
while [ ! -e /tmp/image_weather_script.jpg ]; do
	sleep 3
done
echo "/tmp/image_weather_script.jpg"
