import board
import time
import touchio
import pulseio
from adafruit_motor import servo

touch_A1 = touchio.TouchIn(board.A1)
touch_A5 = touchio.TouchIn(board.A5)
pwm = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

my_servo = servo.Servo(pwm)
angle = 6
while True:
    if touch_A1.value: #when A1 is touched "a1 been touched" is printed on serial monitor
        print("A1 been touched")
        angle += 1


    if touch_A5.value: #when A5 is touched "a5 been touched" is printed on the serial monitor
        print("A5 been touched")
        angle -= 1
    if angle > 180:
        angle = 180
    if angle < 0:
        angle = 0
    my_servo.angle = angle