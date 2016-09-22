import RPi.GPIO as GPIO
import time
ports=[3,]

def init():
    GPIO.setmode(GPIO.BOARD)
    for item in ports:
        GPIO.setup(item,GPIO.OUT)

def sethigh(port):
    try:
        GPIO.output(port,GPIO.HIGH)
    except Exception,e:
        return e
    return "ok"

def setlow(port):
    try:
        GPIO.output(port,GPIO.LOW)
    except Exception,e:
        return e
    return "ok"