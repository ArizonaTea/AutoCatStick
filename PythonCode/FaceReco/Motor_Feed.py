import RPi.GPIO as GPIO
import time

class motor_feed():
    def __init__(self):
        pass
        
    def run(self):
        ENA = 5
        IN1 = 13
        IN2 = 6
        #GPIO.setmode(GPIO.BCM)
        GPIO.setup(ENA,GPIO.OUT)
        GPIO.setup(IN1,GPIO.OUT)
        GPIO.setup(IN2,GPIO.OUT)
        freq = 500
        speed = 0
        pwm = GPIO.PWM(ENA, freq)
        pwm.start(speed)                     
        GPIO.output(IN1, False)
        GPIO.output(IN2, True)
        pwm.ChangeDutyCycle(25)
        time.sleep(2)
        GPIO.cleanup(ENA)
        GPIO.cleanup(IN1)
        GPIO.cleanup(IN2)
        return

if __name__ == '__main__':
    ms = motor_feed()
    ms.run()