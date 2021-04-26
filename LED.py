import RPi.GPIO as GPIO
import time
from tkinter import *

window = Tk()
window.title("test")

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)


var = IntVar()

def LIGHT_ON():
        GPIO.output(17,GPIO.LOW)
        GPIO.output(18, GPIO.LOW)
        GPIO.output(27, GPIO.LOW)
        if(var.get() == 1):
                GPIO.output(17, GPIO.HIGH)
        elif(var.get() == 2):
                GPIO.output(18, GPIO.HIGH)
        elif(var.get() == 3):
                GPIO.output(27, GPIO.HIGH)

Radiobutton(window, text='Red', variable = var, value=3, command=LIGHT_ON).pack(side = TOP, ipady = 5)
Radiobutton(window, text='Green', variable = var, value=2, command=LIGHT_ON).pack(side = TOP, ipady = 5)
Radiobutton(window, text='Blue', variable = var, value=1, command=LIGHT_ON).pack(side = TOP, ipady = 5)


def on_close():
        GPIO.output(17,GPIO.LOW)
        GPIO.output(18, GPIO.LOW)
        GPIO.output(27, GPIO.LOW)
        window.destroy()


window.protocol("WM_DELETE_WINDOW", on_close)
window.mainloop()
