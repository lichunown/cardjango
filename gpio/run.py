import RPi.GPIO as GPIO
import time
from . import port
# class Car():
#     def __init__(self):
#         print "car init"
#         self.left=[35,37]
#         self.right=[36,38]
#         port.sethigh(self.left[0])
#         port.sethigh(self.left[1])
#         port.sethigh(self.right[0])
#         port.sethigh(self.right[1])
#     def leftgo(self):
#         port.setlow(self.left[0])
#         port.sethigh(self.left[1])
#     def leftback(self):
#         port.setlow(self.left[1])
#         port.sethigh(self.left[0])        
#     def rightgo(self):
#         port.setlow(self.right[0])
#         port.sethigh(self.right[1])
#     def rightback(self):
#         port.setlow(self.right[1])
#         port.sethigh(self.right[0])  
#     def stopleft(self):
#         port.sethigh(self.left[0])
#         port.sethigh(self.left[1])   
#     def stopright(self):
#         port.sethigh(self.right[0])
#         port.sethigh(self.right[1])            
#     def stop(self):
#         port.sethigh(self.left[0])
#         port.sethigh(self.left[1])
#         port.sethigh(self.right[0])
#         port.sethigh(self.right[1])        
#     def run(self):
#         self.leftgo()
#         self.rightgo()

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
        self.rightgo(rightspeed,devright)
        self.leftgo(leftspeed,devleft)
        return (devleft,devleft)
    def stop(self):
        self.leftstop()
        self.rightstop()
    def back(self,leftspeed = 100,rightspeed = 100,devleft = None,devright = None):
        devleft = self.DEVIleft if not devleft else int(devleft)
        devright = self.DEVIright if not devright else int(devright)        
        self.leftback(leftspeed,devleft)
        self.rightback(rightspeed,devright)
        return (devleft,devleft)
    def leftgo(self,speed = 100,dev = None):
        dev = self.DEVIleft if not dev else int(dev)
        self.left1.ChangeDutyCycle(self._getspeed(speed,dev))
        self.left2.ChangeDutyCycle(100)  
        return dev
    def leftback(self,speed = 100,dev = None):
        dev = self.DEVIleft if not dev else int(dev)
        self.left1.ChangeDutyCycle(100)                      
        self.left2.ChangeDutyCycle(self._getspeed(speed,dev))
        return dev        
    def leftstop(self):
        self.left1.ChangeDutyCycle(100)                      
        self.left2.ChangeDutyCycle(100)      
    def rightgo(self,speed = 100,dev = None):
        dev = self.DEVIright if not dev else int(dev)       
        self.right1.ChangeDutyCycle(self._getspeed(speed,dev))
        self.left2.ChangeDutyCycle(100) 
        return dev        
    def rightback(self,speed = 100,dev = None):
        dev = self.DEVIright if not dev else int(dev)            
        self.right1.ChangeDutyCycle(100)
        self.right2.ChangeDutyCycle(self._getspeed(speed,dev))
        return dev        
    def rightstop(self):
        self.right1.ChangeDutyCycle(100)                      
        self.right2.ChangeDutyCycle(100)        
