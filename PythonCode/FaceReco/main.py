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

class auto_catstick_process(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.Detec = ''
    
    def run(self):
        global JobID
        try:
            while True:
                #Turn On
                #if not GPIO.input(25):
                #    flag = not flag
                #    GPIO.output(18, flag)
                #print("check the flag", flag)
                GPIO.output(18, flag)
                if flag:
                    #Start Detecting
                    #test = CatFaceDetec.catfacedetect()
                    self.Detec = CatFaceDetec.catfacedetect()
                    self.Detec.detect(JobID)

                    #Motor Run
                    #Place Holder/Use LED for now
                    if flag:
                        GPIO.output(23, True)
                        time.sleep(10)
                        GPIO.output(23, False)

                    #Process End
                    self.Detec.KillProcess()
                    JobID += 1
        except:
            self.Detec.KillProcess()
            GPIO.output(18, False)
            GPIO.output(23, False)
            print("Process Stopped")
            
    def kill(self):
        if self.Detec != '':
            self.Detec.KillProcess()
        
    
class control(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        global flag 
        while True:
            #time.sleep(1)
            if not GPIO.input(25):
                flag = not flag
                time.sleep(1)
            #print('Current Status is: ', flag)

if __name__ == '__main__':
    try:
        app = auto_catstick_process()
        con = control()
        con.start()
        app.start()
        while True:
            #time.sleep(1)
            if not flag:
                app.kill()
                #print('Auto Killed Process')
    except:
        GPIO.cleanup()
        print("Program Stop")
    