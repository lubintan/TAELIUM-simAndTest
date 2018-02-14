#!/bin/bash
while true
do
	python skynetLocal_master.py
	sleep 1800
	pkill -f python
	pkill -f selenium
	pkill -f selenium
	pkill -f firefox
	pkill -f firefox
	pkill -f geckodriver
	pkill -f geckodriver
	pkill -f geckodriver
	sleep 5	 
done

			