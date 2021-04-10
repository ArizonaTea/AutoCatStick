import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(25,GPIO.IN)
GPIO.setup(23,GPIO.OUT)

GPIO.cleanup()