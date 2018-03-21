#!/bin/bash
while true
do
	python skynetLocal_master.py &
	sleep 1800
	pkill -9 -f -e python
	sleep 2
	pkill -9 -f -e selenium
	sleep 2
	pkill -9 -f -e firefox
	sleep 2
	pkill -9 -f -e geckodriver
	sleep 5	 
done

			