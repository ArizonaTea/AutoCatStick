import CatFaceDetec
import RPi.GPIO as GPIO
import time
import threading

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(25,GPIO.IN)
GPIO.setup(23,GPIO.OUT)
flag = False
JobID = 0

class auto_catstick_process():
    def __init__(self):
        pass
    
    def run(self):
        global JobID
        try:
            while True:
                #Turn On
                #if not GPIO.input(25):
                #    flag = not flag
                #    GPIO.output(18, flag)
                GPIO.output(18, flag)
                if flag:
                    #Start Detecting
                    test = CatFaceDetec.catfacedetect()
                    test.detect(JobID)

                    #Motor Run
                    #Place Holder/Use LED for now
                    GPIO.output(23, True)
                    time.sleep(10)
                    GPIO.output(23, False)

                    #Process End
                    test.KillProcess()
                    JobID += 1
                else:
                    return
        except:
            test.KillProcess()
            GPIO.output(18, False)
            GPIO.output(23, False)
            print("Process Stopped")
    
class control(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        global flag 
        while True:
            time.sleep(1)
            if not GPIO.input(25):
                flag = not flag
                time.sleep(1)
            print('Current Status is: ', flag)

class autokill(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        while True:
            time.sleep(10)
            if not flag:
                kill = CatFaceDetec.catfacedetect()
                kill.KillProcess()
                print('Process Killed')

if __name__ == '__main__':
    app = auto_catstick_process()
    con = control()
    ak = autokill()
    con.start()
    #ak.start()
    while True:
        app.run()
    
    