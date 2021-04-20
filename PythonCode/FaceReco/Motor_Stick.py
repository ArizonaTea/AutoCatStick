import RPi.GPIO as GPIO
import time

class motor_stick():
    def __init__(self):
        pass
        
    def run(self, stime):
        ENA = 17
        IN1 = 27
        IN2 = 22
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(ENA,GPIO.OUT)
        GPIO.setup(IN1,GPIO.OUT)
        GPIO.setup(IN2,GPIO.OUT)
        freq = 500
        speed = 0
        pwm = GPIO.PWM(ENA, freq)
        pwm.start(speed)                     
        GPIO.output(IN1, False)
        GPIO.output(IN2, True)
        for speed in range(50, 100, 5):
            pwm.ChangeDutyCycle(speed)
            time.sleep(stime)
        GPIO.output(IN1, True)
        GPIO.output(IN2, False)
        for speed in range(50, 100, 5):
            pwm.ChangeDutyCycle(speed)
            time.sleep(stime)
        GPIO.cleanup(ENA)
        GPIO.cleanup(IN1)
        GPIO.cleanup(IN2)
        return
        
        
if __name__ == '__main__':
    ms = motor_stick()
    ms.run(1)
