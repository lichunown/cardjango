import RPi.GPIO as GPIO
import time

ports=[x for x in range(1,27)]

def init():
    GPIO.setmode(GPIO.BOARD)
    for item in ports:
        try:
            GPIO.setup(item,GPIO.OUT)
        except Exception,e:
            print "%d error:%s" % (item,e)

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

def changestat(port):
    try:
        if GPIO.input(port):
            GPIO.output(port,GPIO.LOW)
        else:
            GPIO.output(port,GPIO.HIGH) 
    except Exception,e:
        return e
    return "ok"