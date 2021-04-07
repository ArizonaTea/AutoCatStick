from picamera import PiCamera
import RPi.GPIO as GPIO
import time

camera = PiCamera()
camera.rotation = 180

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(25,GPIO.IN)
count = 0

while True:
    if GPIO.input(25):
        GPIO.output(18, False)
    else:
        GPIO.output(18, True)
        path = '/home/pi/Desktop/image'+ str(count) + '.jpg'
        camera.capture(path)
        count = count + 1
        print('Photo taken, stored at '+ path)