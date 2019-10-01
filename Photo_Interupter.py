import board
import time
from digitalio import DigitalInOut, Direction, Pull


counter = 0
interupts = 0
photo = DigitalInOut(board.D7)
photo.direction = Direction.INPUT
photo.pull = Pull.UP
initial = time.monotonic()

while True:
    now = time.monotonic()
    if time.monotonic() % 4 == 0:
        print("the number of interrupts is ", counter)
    if photo.value and interupts == 0:
        interupts = 1
        initial = now
        counter = counter +1


    elif not photo.value:
        interupts = 0