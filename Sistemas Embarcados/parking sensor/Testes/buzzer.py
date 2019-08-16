import RPi.GPIO as GPIO 
import time 
import threading as th

class Buzzer():

    def __init__(self, pin, freq, level):
        self.level = level
        GPIO.setmode(GPIO.BCM) 
        GPIO.setup(pin, GPIO.OUT) 
        self.pwm = GPIO.PWM(pin,freq)
                
    def buzz(self, pitch, DC):
        self.pwm.ChangeFrequency(pitch)
        self.pwm.start(DC)
        time.sleep(2)
        self.pwm.stop()
        time.sleep(1)
    def stopBuzz():
        self.pwm.stop()

def main():
    b = Buzzer(18, 100,0)
    b.buzz(100,0)
    time.sleep(2)
    print('1')
    b.buzz(1000,50)
    time.sleep(2)
    print('2')
    b.buzz(2000,80)
    time.sleep(2)
    print('3')
    b.buzz(3000,100)
    time.sleep(2)
    print('4')
main()
