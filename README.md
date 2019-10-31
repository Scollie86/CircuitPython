# README

# Hello CircuitPython
### Objective
Make an LED fade in and out on CircuitPython.
### Code
    import time
    import board
    import pulseio



    digital_leds = DigitalInOut(board.D2)
    digital_leds.direction = Direction.OUTPUT


    while True:


        # reverses the    direction of the fading at the ends of the fade:
    if brightness <= 0:
        fade_amount = -fade_amount
        counter += 1
    elif brightness >= 65535:
        fade_amount = -fade_amount
        counter += 1
### Lesson
We learned to use While True instead of using loops. This was also my first time using the Metro and CircuitPython so I got started learning some of it.  
### Pictures

# CircuitPython Servo
### Objective
Make a servo move right or left depending on which wire is touched.
### Code
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
    
    ### Lesson
    I learned how to do this assignment by using Capacitive touch on the metro. I was not very familiar with coding servos, especially on CircuitPython so that was really helpful.
### Pictures

# CicuitPython LCD
### Objective
Use a button to make a variable go up and down on a LCD Screen.
### Code
    import board
    import time
    from digitalio import DigitalInOut, Direction, Pull
    from lcd.lcd import LCD
    from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
    from lcd.lcd import CursorMode


    button = DigitalInOut(board.D2)
    button.direction = Direction.INPUT
    button.pull = Pull.DOWN
    switch = DigitalInOut(board.D3)
    switch.direction = Direction.INPUT
    switch.pull = Pull.DOWN

    clicks = 0
    clicks2 = 1
    lcd = LCD(I2CPCF8574Interface(0x27), num_rows=2, num_cols=16)


    while True:
        #if not button.value and oldButton:
            lcd.set_cursor_pos(0,0)
            lcd.print("Switch")
            lcd.set_cursor_pos(1,0)
            lcd.print("presses")

            if switch.value:
                clicks2 =-1

                lcd.set_cursor_pos(0,7)
                lcd.print(" Down ")
                lcd.print("  ")
                lcd.set_cursor_pos(0,7)
            if switch.value and clicks2 == -1:
                clicks2 = 1
                lcd.set_cursor_pos(0,7)
                lcd.print(" Up ")
                lcd.print("  ")
                lcd.set_cursor_pos(0,7)
            if button.value: #and lastbuttonvalue == 1:

                lcd.set_cursor_pos(1,8)

                clicks += clicks2
                lcd.print(str(clicks))
                lcd.print("  ")
                lcd.set_cursor_pos(1,8)
        #oldButton = button.value
### Lesson
Learned how to use the new code to make the LCD work. I Learned how useful the backback is for the LCD screen.
### Pictures
# Photo Interrupters
### Objective
Used a Photointerrupter to display the interruptions every four seconds.
### Code
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
### Lesson
I learned how to make something register every four seconds which was a struggle. 
### Pictures
# Distance Sensor
### Objective
We used a HC-SR04 to make the rgb LED change colors according to the distance of an object.
### Code
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

    RED = (255, 0, 0)
    PURPLE = (180, 0, 255)
    BLUE = (0, 0, 255)
    CYAN = (0, 255, 255)
    GREEN = (0, 255, 0)

    while True:
        try:
            distance = sonar.distance
            print((distance))

            if distance > 0 and distance <= 7:
                pixels.fill(RED)
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

### Lesson
I learned how to change the colors and the code for different rgb colors. I learned that the colors are just like in real life and you can add each of the three basic colors to make almost any color.
### Pictures
# Hello Git
### Objective
We dowloaded the Git Bash app and edited my ReadME.md.
### Lesson
I learned how to use Git Bash and how to edit my readME.md through the Git Bash app.
### Pictures
# Hello GitHub
### Objective
We created a repository to put all of our assignments in.
### Lesson
I learned a new way to edit my GitHub. I also found it very useful when starting to organize my assignments.
### Pictures
# Forks and Clones
### Objective
We forked the CHS Sigma account and made a copy for our own account.
### Lesson
I learned how to get to other peoples repository. I learned how to fork repositories from the class and clone them.
### Pictures
# Classes, Objects, and Modules
### Objective
Made a library for the rgb LED in one tab while we had another one named main.py.
### Code
    import board
    import time
    import pulseio
    from digitalio import DigitalInOut, Direction, Pull



    class RGB:
        def __init__(self, r, g, b):
            self.r = DigitalInOut(r)
            self.r.direction = Direction.OUTPUT
            self.g = DigitalInOut(g)
            self.g.direction = Direction.OUTPUT
            self.b = DigitalInOut(b)
            self.b.direction = Direction.OUTPUT
        def red(self):
            self.r.value = False
            self.g.value = True
            self.b.value = True
        def green(self):
            self.g.value = False
            self.b.value = True
            self.r.value = True
        def blue(self):
            self.b.value = False
            self.g.value = True
            self.r.value = True
        def cyan(self):
            self.g.value = False
            self.b.value = False
            self.r.value = True
        def magenta(self):
            self.r.value = False
            self.b.value = False
            self.g.value = True
        def yellow(self):
            self.b.value = True
            self.g.value = False
            self.r.value = False
### Lesson
I learned how to make libraries on CircuitPython.
### Pictures
# Hello vs Code
### Objective
We learned how to print something in the serial monitor of vs code.
### Code
    import time

    while True:
        print("Hello")
        time.sleep(0.1)
### Lesson
I learned how to use vs code when printing code and using it to push and commit something into my GitHub.
### Pictures
# FancyLED
### Objective

### Code

### Lesson

### Pictures