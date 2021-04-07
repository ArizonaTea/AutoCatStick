from picamera import PiCamera
import time

camera = PiCamera()
camera.rotation = 180
camera.start_preview()
time.sleep(10)
camera.stop_preview()
camera.capture('/home/pi/Desktop/image.jpg')

print('End')