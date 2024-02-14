import neopixel
import machine
import utime

strip_pin = machine.Pin(28, machine.Pin.OUT)
FULLBRIGHT = 256
def draw(level : int):
    n = neopixel.NeoPixel(strip_pin, 8)
    
    brightness = int(FULLBRIGHT / 4)
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


for i in range(9):
    draw(i)
    utime.sleep_ms(1000)

n = neopixel.NeoPixel(strip_pin, 8)
n.fill((0,0,0))
n.write()