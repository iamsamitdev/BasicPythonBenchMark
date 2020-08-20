
from machine import Pin, PWM
from time import sleep

Red = PWM(Pin(5), 5000)
Green = PWM(Pin(4), 5000)
Blue = PWM(Pin(15), 5000)

while True:

    # Red
    Red.duty(255)
    Green.duty(0)
    Blue.duty(0)
    sleep(1)

    # Green
    Red.duty(0)
    Green.duty(255)
    Blue.duty(0)
    sleep(1)

    # Blue
    Red.duty(0)
    Green.duty(0)
    Blue.duty(255)
    sleep(1)

    # Yellow
    Red.duty(255)
    Green.duty(255)
    Blue.duty(0)
    sleep(1)

    # Magenta
    Red.duty(0)
    Green.duty(255)
    Blue.duty(255)
    sleep(1)

    # Cyan
    Red.duty(255)
    Green.duty(0)
    Blue.duty(255)
    sleep(1)
