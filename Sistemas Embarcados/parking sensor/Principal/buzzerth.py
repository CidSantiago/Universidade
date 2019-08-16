import RPi.GPIO as GPIO 
import time 

def init_buzzer(pin,freq):
    GPIO.setmode(GPIO.BCM) 
    GPIO.setup(pin, GPIO.OUT) 
    buzzer = GPIO.PWM(pin,100)
    return buzzer

def buzz(pin, duration,DC):
    #p.ChangeFrequency(pitch)
    bz=GPIO.PWM(pin,100)
    bz.start(DC)
    time.sleep(0.5)
    bz.stop()
    time.sleep(duration)
'''b=init_buzzer(18,100)
buzz(18,2,95)
buzz(18,2,95)
buzz(18,2,95)
time.sleep(1)
print('1')
buzz(18,3,95)
buzz(18,3,95)
buzz(18,3,95)
print('2')
buzz(18,4,95)
buzz(18,4,95)
buzz(18,4,95)'''
