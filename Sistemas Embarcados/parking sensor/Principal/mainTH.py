import hcsr04
import screen
from datetime import datetime
import time
import numpy as np
import buzzerth as bz
import threading as th

global min_dist
min_dist=200

def func():
    #global min_dist
    #print('entrou')
    #print('to no while')
    #print('min_dist= '+str(min_dist))
    if 75<min_dist<=150:
        for i in range(3):
            bz.buzz(18,2,95)
        #print('while1')
    if 30<min_dist<=75:
        #print('while2')
        for i in range(4):
            bz.buzz(18,0.8,95)
    if min_dist<=30:
        #print('while3')
        for i in range(5):
            bz.buzz(18,0.2,95)


def main():
    global min_dist
    sensor1 = hcsr04.HCSR04(4,19)
    sensor2 = hcsr04.HCSR04(16,26)
    sensor3 = hcsr04.HCSR04(13,6)
    nokia = screen.Screen()
    f = 255*np.ones(12)
    nokia.print_bars(f)
    z = bz.init_buzzer(18, 100)
    b=th.Thread(target = func, args =())
    while(True):
        dists = []
        dist1 = sensor1.distance_cm()
        if 150 < dist1:
            f[0] = 255
            f[3] = 255
            f[6] = 255
            f[9] = 255
            nokia.print_bars(f)
        elif 75 < dist1 <= 150:
            #b.buzz(100,95)
            f[0] = 0
            f[3] = 255
            f[6] = 255
            f[9] = 255
            nokia.print_bars(f)
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
            f[0] = 0
            f[3] = 0
            f[6] = 0
            f[9] = 0
            nokia.print_bars(f)

        dist2 = sensor2.distance_cm()
        
        if 150 < dist2:
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
        
        if dist1 != -1:
            dists.append(dist1)        
        if dist2 != -1:
            dists.append(dist2)
        if dist3 != -1:
            dists.append(dist3)
            
        min_dist = min(dists)
        #print('ta dando'+ str(min_dist))
        distance = str(min_dist) + " cm"
        position = (20,10)
        nokia.write_text(distance, position)
        if(not b.is_alive()):
            #print('morta')
            b=th.Thread(target = func, args =())
            b.start()
            
        #b.stopBuzz

main()
