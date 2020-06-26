import time
import board
import math
import digitalio
from analogio import AnalogIn


import adafruit_dotstar
ledin = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
ledin.brightness = 0.01
ledin[0] = (0, 255, 0)


# LED
led = digitalio.DigitalInOut(board.D0)
led.direction = digitalio.Direction.OUTPUT

# RPR 220
analog_in = AnalogIn(board.A3)
n = 0
ref = analog_in.value

last_clock = 0
clock = 0
cycle = 0
Ti = 0
Tf = 0
cycles = 0
nb_periodes = 0
nb_periodes_total = 10




ref = 20000
print(analog_in.value)

while nb_periodes <= nb_periodes_total:
    led.value = False
    debut = 0
    fin = 0
    plot = ref
    while analog_in.value > ref*1.5:
        led.value = True
        if debut == 0:
            debut = time.monotonic()
            print((plot*2,))

       
        #print((plot*2,))
        #print((analog_in.value,))
        #print(analog_in.value)
        #time.sleep(0.04)



    fin = time.monotonic()

    #print('debut= ',debut)
    #print('fin= ',fin)

    if debut != 0:


        if cycles % 2 == 0:
            nb_periodes = nb_periodes + 1
            clock = debut + (fin-debut)/2
            if Ti == 0:
                Ti = clock

            Tf = clock

        cycles = cycles + 1
        plot = plot*2




    #print('--------------')
    #print('Ref: ', ref)
    #print('Time:', time.monotonic())
    #print('Cycles: ', cycles)
    #print('Ti= ',Ti)
    #print('Tf= ',Tf)
    #print('Clock= ',clock)
    print((plot,))
    #print((analog_in.value,))
    
    time.sleep(0.02)

print(analog_in.value)
T = (Tf - Ti) / nb_periodes_total
l = (T**2 * 9.81) / (4*math.pi**2)
print('Temps total: ', Tf - Ti)
print('Periode : ',T,'s')
print('Longueur du fil : ',l,'m')

