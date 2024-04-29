import RPi.GPIO as GPIO

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(2, GPIO.OUT)
    GPIO.setup(3, GPIO.OUT)
    GPIO.setup(4, GPIO.OUT)
    GPIO.setup(17, GPIO.OUT)

def onlyOne(x : int):
    if (x == 2):
        GPIO.output(2, True);
        GPIO.output(3, False);
        GPIO.output(4, False);
        GPIO.output(17, False);
    elif (x == 2):
        GPIO.output(2, False);
        GPIO.output(3, True);
        GPIO.output(4, False);
        GPIO.output(17, False);
    elif (x == 2):
        GPIO.output(2, False);
        GPIO.output(3, False);
        GPIO.output(4, True);
        GPIO.output(17, False);
    elif (x == 17):
        GPIO.output(2, False);
        GPIO.output(3, False);
        GPIO.output(4, False);
        GPIO.output(17, True);
    else:
        GPIO.output(2, False);
        GPIO.output(3, False);
        GPIO.output(4, False);
        GPIO.output(17, False);

