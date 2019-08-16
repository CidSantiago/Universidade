import hcsr04
import screen
from datetime import datetime
import time
import numpy as np
import buzzer
import RPi.GPIO as GPIO 
def main():
    
    sensor1 = hcsr04.HCSR04(4,19)
    sensor2 = hcsr04.HCSR04(16,26)
    #sensor3 = hcsr04.HCSR04(x,y)
    GPIO.setmode(GPIO.BCM) 
    GPIO.setup(18, GPIO.OUT) 
    pwm = GPIO.PWM(18,100)
    nokia = screen.Screen()
    f = 255*np.ones(12)
    nokia.print_bars(f)
    DC=95
    #b = buzzer.Buzzer(18, 100,0)
    #b.stop()
        
    while(True):
        dists = []
        dist1 = sensor1.distance_cm()
        if 150 < dist1:
            pwm.stop()
            f[0] = 255
            f[3] = 255
            f[6] = 255
            f[9] = 255
            nokia.print_bars(f)
        elif 75 < dist1 <= 150:
            #b.buzz(100,95)
            pwm.ChangeFrequency(100)
            pwm.start(DC)
            f[0] = 0
            f[3] = 255
            f[6] = 255
            f[9] = 255
            nokia.print_bars(f)
            time.sleep(1)
        elif 50 < dist1 <= 75:
            #b.buzz(700,95)
            f[0] = 0
            f[3] = 0
            f[6] = 255
            f[9] = 255
            nokia.print_bars(f)
        elif 25 < dist1 <= 50:
            #b.buzz(2000,95)
            f[0] = 0
            f[3] = 0
            f[6] = 0
            f[9] = 255
            nokia.print_bars(f)
        elif 0 < dist1 < 25:
            #b.buzz(3000,95)
            pwm.ChangeFrequency(1000)
            pwm.start(DC)
            f[0] = 0
            f[3] = 0
            f[6] = 0
            f[9] = 0
            nokia.print_bars(f)
            time.sleep(1)

        dist2 = sensor2.distance_cm()
        
        if 150 < dist2:
            pwm.stop()
            f[1] = 255
            f[4] = 255
            f[7] = 255
            f[10] = 255
            nokia.print_bars(f)
        elif 75 < dist2 <= 150:
            f[1] = 0
            f[4] = 255
            f[7] = 255
            f[10] = 255
            nokia.print_bars(f)
        elif 50 < dist2 <= 75:
            f[1] = 0
            f[4] = 0
            f[7] = 255
            f[10] = 255
            nokia.print_bars(f)
        elif 25 < dist2 <= 50:
            f[1] = 0
            f[4] = 0
            f[7] = 0
            f[10] = 255
            nokia.print_bars(f)
        elif 0 < dist2 < 25:
            f[1] = 0
            f[4] = 0
            f[7] = 0
            f[10] = 0
            nokia.print_bars(f)
        '''   
        dist3 = sensor3.distance_cm()
        
        if 150 < dist3:
            f[2] = 255
            f[5] = 255
            f[8] = 255
            f[11] = 255
            nokia.print_bars(f)
        elif 75 < dist3 <= 150:
            f[2] = 0
            f[5] = 255
            f[8] = 255
            f[11] = 255
            nokia.print_bars(f)
        elif 50 < dist3 <= 75:
            f[2] = 0
            f[5] = 0
            f[8] = 255
            f[11] = 255
            nokia.print_bars(f)
        elif 25 < dist3 <= 50:
            f[2] = 0
            f[5] = 0
            f[8] = 0
            f[11] = 255
            nokia.print_bars(f)
        elif 0 < dist3 < 25:
            f[2] = 0
            f[5] = 0
            f[8] = 0
            f[11] = 0
            nokia.print_bars(f)
        '''
        if dist1 != -1:
            dists.append(dist1)        
        if dist2 != -1:
            dists.append(dist2)
        #if dist3 != -1:
         #   dists.append(dist3)
            
        min_dist = min(dists)
        
        distance = str(min_dist) + " cm"
        position = (20,10)
        nokia.write_text(distance, position)
        #b.stopBuzz

main()
