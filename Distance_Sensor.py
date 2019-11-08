import time
import neopixel
import board
from adafruit_hcsr04 import HCSR04
trig = board.D2
echo = board.D3
sonar = HCSR04(trig, echo)
pixel_pin = board.NEOPIXEL
num_pixels = 1
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3)

RED = (255, 0, 0) #RGB code for Red
PURPLE = (180, 0, 255)  #RGB code for Purple
BLUE = (0, 0, 255) #RGB code for Blue
CYAN = (0, 255, 255)#RGB code for Cyan
GREEN = (0, 255, 0)#RGB code for Green

while True:
    try:
        distance = sonar.distance
        print((distance)) #shows distance in the serial monitor

        if distance > 0 and distance <= 7:
            pixels.fill(RED) # inbetween 0 and 7 it shows Red on the RGB
            pixels.show()
        if distance > 7 and distance <= 14:
            pixels.fill(PURPLE)
            pixels.show()
        if distance > 14 and distance <= 21:
            pixels.fill(BLUE)
            pixels.show()
        if distance > 21 and distance <= 28:
            pixels.fill(CYAN)
            pixels.show()
        if distance > 28 and distance <= 35:
            pixels.fill(GREEN)
            pixels.show()
    except RuntimeError:
        print("Retrying!")
        pass
        time.sleep(.2)



