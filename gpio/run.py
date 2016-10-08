import RPi.GPIO as GPIO
import time
from . import port
class Car():
    def __init__(self):
        print "car init"
        self.left=[35,37]
        self.right=[36,38]
        port.sethigh(self.left[0])
        port.sethigh(self.left[1])
        port.sethigh(self.right[0])
        port.sethigh(self.right[1])
    def leftgo(self):
        port.setlow(self.left[0])
        port.sethigh(self.left[1])
    def leftback(self):
        port.setlow(self.left[1])
        port.sethigh(self.left[0])        
    def rightgo(self):
        port.setlow(self.right[0])
        port.sethigh(self.right[1])
    def rightback(self):
        port.setlow(self.right[1])
        port.sethigh(self.right[0])  
    def stopleft(self):
        port.sethigh(self.left[0])
        port.sethigh(self.left[1])   
    def stopright(self):
        port.sethigh(self.right[0])
        port.sethigh(self.right[1])            
    def stop(self):
        port.sethigh(self.left[0])
        port.sethigh(self.left[1])
        port.sethigh(self.right[0])
        port.sethigh(self.right[1])        
    def run(self):
        self.leftgo()
        self.rightgo()

class Car2():
    def __init__(self):
        print "car init"
        self.DEVIleft = 0  #deviation
        self.DEVIright = 0  #deviation
        self.left=[35,37]
        self.right=[36,38]
        self.left1 = GPIO.PWM(self.left[0],500)
        self.left2 = GPIO.PWM(self.left[1],500) 
        self.right1 = GPIO.PWM(self.right[0],500)
        self.right2 = GPIO.PWM(self.right[1],500)         
        self.left1.ChangeDutyCycle(100)
        self.left2.ChangeDutyCycle(100)    
        self.right1.ChangeDutyCycle(100)
        self.right2.ChangeDutyCycle(100)          
    def go(self,devleft = self.DEVIleft,devright = self.DEVIright):
        self.left1.ChangeDutyCycle(devleft)
        self.right1.ChangeDutyCycle(devright)
        self.left2.ChangeDutyCycle(100)  
        self.right2.ChangeDutyCycle(100) 
    def leftgo(self,dev = self.DEVIleft):
        self.left1.ChangeDutyCycle(dev)
        self.left2.ChangeDutyCycle(100)  
    def leftback(self,dev = self.DEVIleft):
        self.left1.ChangeDutyCycle(100)                      
        self.left2.ChangeDutyCycle(dev)
    def leftstop(self):
        self.left1.ChangeDutyCycle(100)                      
        self.left2.ChangeDutyCycle(100)      
    def rightgo(self,dev = self.DEVIright):
        self.right1.ChangeDutyCycle(dev)
        self.left2.ChangeDutyCycle(100)        
