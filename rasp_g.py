#!/usr/bin/env python

import sys
import RPi.GPIO as GPIO
import time
import os
import subprocess

GPIO.setmode(GPIO.BCM)
gpio_pin = 26
GPIO.setup(gpio_pin, GPIO.OUT)

try:
#subprocess.call('aplay /usr/share/sounds/alsa/Side_Right.wav',shell=True)
	p=GPIO.PWM(gpio_pin, 1000)
	p.start(100)
	p.ChangeDutyCycle(10)
	time.sleep(0.3)
	p.stop()
	p.start(80)
	p.ChangeDutyCycle(50)
	time.sleep(0.3)
	p.stop()
finally:
	GPIO.cleanup()
