#!/bin/bash
# A quick file to help facilitate looping the non-loopable
# nature of the Twister reactor using CrawlerProcess in the
# corresponding Python script (update every minute)
#
# We should consider integrating this looping function into
# the rest of the miniWeather.py script!! 
#
# (however, for quick-and-easy looping crawls, we can split
# the script into a repeating bash script and a Python script
# so that a file containing what we have scraped can be updated
#  continuously)

while true; do
	python3 covidCounter.py
	sleep 60
done

# Note that the advantage of using a bash script to automate this
# is that we get system-level access over running this script in
# the background of the OS
#
# (to run this in the background when running, you can do & after
# the command)

