import RPi.GPIO as GPIO 
import time 

def init_buzzer(pin,freq):
    GPIO.setmode(GPIO.BCM) 
    GPIO.setup(18, GPIO.OUT) 
    buzzer = GPIO.PWM(18,100)
    return buzzer

def buzz(pitch, duration,DC,p):
    p.ChangeFrequency(pitch)
    p.start(DC)
    time.sleep(duration)
    p.stop()
    time.sleep(1)
b=init_buzzer(18,100)
buzz(100,2,95,b)
