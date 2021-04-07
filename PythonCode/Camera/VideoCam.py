from picamera import PiCamera
import RPi.GPIO as GPIO
import time

camera = PiCamera()
camera.rotation = 180
camera.resolution = (1920,1080)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(25,GPIO.IN)
count = 0
flag = 0

while True:
    if GPIO.input(25):
        if flag == 1:
            GPIO.output(18, True)
        else:
            GPIO.output(18, False)
    else:
        if flag == 0:
            path = '/home/pi/Desktop/vedio'+ str(count) + '.h264'
            camera.start_preview()
            GPIO.output(18, True)
            camera.start_recording(path)
            flag = 1
            time.sleep(1)
        else:
            camera.stop_recording()
            camera.stop_preview()
            count = count + 1
            print('Vedio Recorded, stored at '+ path)
            GPIO.output(18, False)
            flag = 0
            time.sleep(1)
