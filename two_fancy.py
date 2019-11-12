from FancyLED import FancyLED #pylint: disable=import-error
import board #pylint: disable=import-error
import time #pylint: disable=import-error

fancy1 = FancyLED(board.D2,board.D3,board.D4)
fancy2 = FancyLED(board.D5,board.D6,board.D7)

while True:
    print("working")
    for i in range(0, 3):
        fancy1.alternate()
        time.sleep(1)
    for i in range(0,3):
        fancy2.blink()
        time.sleep(1)
    for i in range(0,3):
        fancy1.chase()
    for i in range(0, 15):
        fancy2.sparkle()