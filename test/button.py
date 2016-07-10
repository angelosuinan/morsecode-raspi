import time
from time import sleep
'''
beg_ts = time.time()
sleep(1)
end_ts = time.time()
print("elapsed time: %f" % (end_ts - beg_ts))
answer = str(round(answer, 2))

'''

from gpiozero import Button

class BtnMorse(object):
    pat=""
    def __init__(self):
        print("asa")

    def make_dot(self):
        self.pat+="."

    def make_dash(self):
        self.pat+="-"
class InputMorse(object):
    pattern = ""
    def start(self, before,start):
        while True:
            self.button.wait_for_release()
            secprsd =  self.get_present(start) - before
            if secprsd >=0.9 and secprsd <= 1.5:
                print (secprsd , "    dot")
                self.add_dot()
                return self.begin(True)
            if secprsd >=2.25:
                print (secprsd , "   dash")
                self.add_dash()
                return self.begin(True)


    def add_dot(self):
        self.pattern+="."
        print (self.pattern)
        return
    def add_dash(self):
        self.pattern+="-"
        print (self.pattern)
        return
    def roundoff(self):
        return (round(time.time(),2))
    def get_present(self, start):
        return self.roundoff() - start



    def begin(self, nextWord=False):
        start= self.roundoff()
        while True:
            timeout = self.get_present(start)
            if self.button.is_pressed:
                before = round(self.get_present(start), 2)
                return self.start(before, start)
            if nextWord == True and timeout >=4:
                print (round(timeout, 2))
                self.pattern = ""
                return self.begin(False)
            if timeout >= 15:
                return
    def __init__(self, number):
        self.button = Button(number)
a = InputMorse(2)
a.begin()


