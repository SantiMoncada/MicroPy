import utime
import neopixel
import machine

strip_pin = machine.Pin(16, machine.Pin.OUT)
FULLBRIGHT = 255
def draw(level : int):
    n = neopixel.NeoPixel(strip_pin, 8)
    
    brightness = int(FULLBRIGHT / 1)
    if(level > 0 ):
        n[0] = (0,0,brightness)

    if(level > 1 ):
        n[1] = (0,0,brightness)

    if(level > 2 ):
        n[2] = (0,0,brightness)

    if(level > 3 ):
        n[3] = (0,0,brightness)

    if(level > 4 ):
        n[4] = (0,brightness,0)

    if(level > 5 ):
        n[5] = (0,brightness,0)

    if(level > 6 ):
        n[6] = (brightness,0,0)
    
    if(level > 7 ):
        n[7] = (brightness,0,0)

    n.write()


trigger = machine.Pin(15,machine.Pin.OUT)
echo = machine.Pin(14,machine.Pin.IN)
distancia = 0

def Medicion_distancia(tiempo):
    trigger.high()
    utime.sleep(tiempo)
    trigger.low()
       


while True:
    Medicion_distancia(0.0001)
    
    duracion = machine.time_pulse_us(echo, machine.Pin.high)
       
    distancia = (duracion*0.0343)/2
    print('Distancia',distancia,'cm')

    draw(8 - int(distancia/(60/8)))
    utime.sleep_ms(100)
