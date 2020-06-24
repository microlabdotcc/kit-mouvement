import time
import board
import math
import digitalio
from analogio import AnalogIn

# ligne 6-9 : attenuer l'intensite de la diode de la carte
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
T = []
last_clock = 0
clock = 0
cycle = 0
while len(T) < 20:
    led.value = False
    n = n + 1
    if n == 100:
        ref = analog_in.value
        n = 0
    over = []
    while analog_in.value > ref*1.2:
        over.append(time.monotonic())
        time.sleep(0.02)
        print((analog_in.value,))

    if over != []:
        clock = over[len(over)//2]
        cycle = cycle + 1

    if cycle % 2 == 0:
        if clock > last_clock:
            if last_clock == 0:
               last_clock = clock
            else:
                #T.append(clock - last_clock)
                last_clock = clock
                led.value = True


    print(cycle)
    print('T= ',T)
    print((analog_in.value,))
    time.sleep(0.02)

T_av = sum(T) / len(T)
l = (T_av**2 * 9.81) / (4*math.pi**2)
print('Periode : ',T_av,'s')
print('Longueur du fil : ',l,'m')
