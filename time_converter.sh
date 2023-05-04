#!/bin/bash


while true 
do
	clear
	# Convert local time to EAT
	eat=$(TZ="Africa/Nairobi" date +"%Y-%m-%d %H:%M:%S")
	echo "EAT: $eat"

	# Convert local time to WAT
	wat=$(TZ="Africa/Lagos" date +"%Y-%m-%d %H:%M:%S")
	echo "WAT: $wat"

	# Convert local time to GMT
	gmt=$(TZ="GMT" date +"%Y-%m-%d %H:%M:%S")
	echo "GMT: $gmt"
	sleep 60
done

