#!/bin/bash

sleep 5

for i in {1..2000}
do
	sleep 40
	xdotool click 1
	echo "совершено $i нажатий."
done	