import time
import board
import pulseio



digital_leds = DigitalInOut(board.D2)
digital_leds.direction = Direction.OUTPUT


while True:


    # reverse the direction of the fading at the ends of the fade:
    if brightness <= 0:
        fade_amount = -fade_amount
        counter += 1
    elif brightness >= 65535: #65525 is the brightest the LED will go
        fade_amount = -fade_amount
        counter += 1
