import RPi.GPIO as GPIO
import time
from . import port
class Car():
    def __init__(self):
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