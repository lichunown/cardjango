import RPi.GPIO as GPIO
import time
from . import port

class Car():
    def __init__(self):
        print "car init"
        self.DEVIleft = 0  #deviation
        self.DEVIright = 0  #deviation
        self.left=[35,37]
        self.right=[36,38]
        try:
            GPIO.setmode(GPIO.BOARD)
        except Exception,e:
            print e
        for item in self.left+self.right:
            try:
                GPIO.setup(item,GPIO.OUT)
            except Exception,e:
                print "%d error:%s" % (item,e)        
        self.left1 = GPIO.PWM(self.left[0],2000)
        self.left2 = GPIO.PWM(self.left[1],2000) 
        self.right1 = GPIO.PWM(self.right[0],2000)
        self.right2 = GPIO.PWM(self.right[1],2000)   
        self.left1.start(100)
        self.left2.start(100)    
        self.right1.start(100)         
        self.right2.start(100)                   
        self.left1.ChangeDutyCycle(100)
        self.left2.ChangeDutyCycle(100)    
        self.right1.ChangeDutyCycle(100)
        self.right2.ChangeDutyCycle(100) 
    def _getspeed(speed,dev):
        speed = int(dev)+100-int(speed)
        speed = 100 if speed>100 else speed 
        speed = 0 if speed<0 else speed
        return speed        
    def go(self,leftspeed = 100,rightspeed = 100,devleft = None,devright = None):
        devleft = self.DEVIleft if not devleft else int(devleft)
        devright = self.DEVIright if not devright else int(devright)
        realrightspeed = self.rightgo(rightspeed,devright)
        realleftspeed = self.leftgo(leftspeed,devleft)
        return (realleftspeed,realrightspeed)
    def stop(self):
        self.leftstop()
        self.rightstop()
    def back(self,leftspeed = 100,rightspeed = 100,devleft = None,devright = None):
        devleft = self.DEVIleft if not devleft else int(devleft)
        devright = self.DEVIright if not devright else int(devright)        
        realleftspeed = self.leftback(leftspeed,devleft)
        realrightspeed = self.rightback(rightspeed,devright)
        return (realleftspeed,realrightspeed)
    def leftgo(self,speed = 100,dev = None):
        dev = self.DEVIleft if not dev else int(dev)
        realspeed = self._getspeed(speed,dev)
        self.left1.ChangeDutyCycle(realspeed)
        self.left2.ChangeDutyCycle(100)  
        return realspeed
    def leftback(self,speed = 100,dev = None):
        dev = self.DEVIleft if not dev else int(dev)
        self.left1.ChangeDutyCycle(100)    
        realspeed = self._getspeed(speed,dev)                          
        self.left2.ChangeDutyCycle(realspeed)
        return realspeed        
    def leftstop(self):
        self.left1.ChangeDutyCycle(100)                      
        self.left2.ChangeDutyCycle(100)      
    def rightgo(self,speed = 100,dev = None):
        dev = self.DEVIright if not dev else int(dev)   
        realspeed = self._getspeed(speed,dev)             
        self.right1.ChangeDutyCycle(realspeed)
        self.left2.ChangeDutyCycle(100) 
        return realspeed        
    def rightback(self,speed = 100,dev = None):
        dev = self.DEVIright if not dev else int(dev)   
        realspeed = self._getspeed(speed,dev)                  
        self.right1.ChangeDutyCycle(100)
        self.right2.ChangeDutyCycle(realspeed)
        return realspeed        
    def rightstop(self):
        self.right1.ChangeDutyCycle(100)                      
        self.right2.ChangeDutyCycle(100)        
