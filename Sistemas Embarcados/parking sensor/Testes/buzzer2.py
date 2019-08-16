import RPi.GPIO as GPIO 
import time 
import threading as th
#import main as mn
class Buzzer(th.Thread):

    def __init__(self, pin, freq):
        GPIO.setmode(GPIO.BCM) 
        GPIO.setup(pin, GPIO.OUT) 
        self.pwm = GPIO.PWM(pin,freq)
        th.Thread.__init__(self)
        self._stop_event = th.Event()
    def run(self):
        print(entrou)
        d=mn.getmin_dist()
        if 75<d<=150:
            while(75<d<=150):
                self.buzz(3,95)
                print('while1')
        if 50<d<=75:
            while(50<d<=75):
                print('while2')
                self.buzz(2,95)
        if 25<d<=50:
            while(25<d<=50):
                print('while3')
                self.buzz(1,95)
    def buzz(self, duration, DC):
        self.pwm.start(DC)
        time.sleep(1)
        self.pwm.stop()
        time.sleep(duration)

def main():
    b = Buzzer(18, 100)
    b.run()
    #buzz(100, 5, 90, b)
