import RPi.GPIO as GPIO

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(2, GPIO.OUT)
    GPIO.setup(3, GPIO.OUT)
    GPIO.setup(4, GPIO.OUT)
    GPIO.setup(14, GPIO.OUT)

def onlyOne(x : int):
    if (x == 0):
        GPIO.output(2, True);
        GPIO.output(3, False);
        GPIO.output(4, False);
        GPIO.output(14, False);
    elif (x == 1):
        GPIO.output(2, False);
        GPIO.output(3, True);
        GPIO.output(4, False);
        GPIO.output(14, False);
    elif (x == 2):
        GPIO.output(2, False);
        GPIO.output(3, False);
        GPIO.output(4, True);
        GPIO.output(14, False);
    elif (x == 3):
        GPIO.output(2, False);
        GPIO.output(3, False);
        GPIO.output(4, False);
        GPIO.output(14, True);
    else:
        GPIO.output(2, False);
        GPIO.output(3, False);
        GPIO.output(4, False);
        GPIO.output(14, False);

