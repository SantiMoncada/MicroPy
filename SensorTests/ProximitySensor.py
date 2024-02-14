from machine import Pin, time_pulse_us
import utime


led = Pin(7,Pin.OUT)

trigger = Pin(15,Pin.OUT)
echo = Pin(14,Pin.IN)
distancia = 0

def Medicion_distancia(tiempo):
    trigger.high()
    utime.sleep(tiempo)
    trigger.low()
       


while True:
    Medicion_distancia(0.0001)
    
    duracion = time_pulse_us(echo, Pin.high)
       
    distancia = (duracion*0.0343)/2
    print('Distancia',distancia,'cm')
    
    utime.sleep(1)
