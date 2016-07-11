import time
from time import sleep

import os
from gpiozero import Button




class InputMorse(object):
    pattern = ""
    CODE = {' ': ' ', 
        "'": '.----.', 
        '(': '-.--.-', 
        ')': '-.--.-', 
        ',': '--..--', 
        '-': '-....-', 
        '.': '.-.-.-', 
        '/': '-..-.', 
        '0': '-----', 
        '1': '.----', 
        '2': '..---', 
        '3': '...--', 
        '4': '....-', 
        '5': '.....', 
        '6': '-....', 
        '7': '--...', 
        '8': '---..', 
        '9': '----.', 
        ':': '---...', 
        ';': '-.-.-.', 
        '?': '..--..', 
        'A': '.-', 
        'B': '-...', 
        'C': '-.-.', 
        'D': '-..', 
        'E': '.', 
        'F': '..-.', 
        'G': '--.', 
        'H': '....', 
        'I': '..', 
        'J': '.---', 
        'K': '-.-', 
        'L': '.-..', 
        'M': '--', 
        'N': '-.', 
        'O': '---', 
        'P': '.--.', 
        'Q': '--.-', 
        'R': '.-.', 
        'S': '...', 
        'T': '-', 
        'U': '..-', 
        'V': '...-', 
        'W': '.--', 
        'X': '-..-', 
        'Y': '-.--', 
        'Z': '--..', 
        '_': '..--.-'}
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
        if self.x:
            start= self.roundoff()
            while True:
                timeout = self.get_present(start)
                if self.button.is_pressed:
                    before = round(self.get_present(start), 2)
                    return self.start(before, start)
                if nextWord == True and timeout >=4:
                    print (round(timeout, 2))
                    for letter, pat in self.CODE.items():
                        if self.pattern == pat :
                            with open('api.txt','w') as f:
                                print (letter,file=f)
                    self.pattern = ""
                    return self.begin(False)
                if timeout >= 15:
                    with open('path', 'w+') as f:
                        print ("TIMEOUT <<<<<<<<<<<<<i")
                    return
    def __init__(self):
        path =os.path.join(os.path.expanduser('~'),'projects', 'morsecode-raspi',
        'morse','raspicode','run.txt')
        self.x=True
        with open(path, 'r') as f:
            line1= f.readline()
            text ="1"
            if "1" in line1:
                self.x =False
                return
        with open(path, 'w+') as f:
            f.write("1")
    button = Button(2)

