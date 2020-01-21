import tkinter
from tkinter import messagebox
import random
from random import randrange


class gui:
    def __init__(self):
        self.window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.window, width=200, height=200)
        self.canvas.pack()
        self.knop1 = tkinter.Button(self.window, text = 'Quit', command=self.window.destroy)
        self.knop1.pack(side='bottom')
        self.canvas.create_line(180, 200, 180, 0)
        a = int(0)
        b = int(0)
        c = int(0)
        d = int(0)
        for k in range(9000):

            a = a + random.randint(1, 9)
            self.canvas.create_line(0, 90, a, 90)
            b = b + random.randint(1, 9)
            self.canvas.create_line(0, 110, b, 110)
            c = c + random.randint(1, 9)
            self.canvas.create_line(0, 130, c, 130)
            d = d + random.randint(1, 9)
            self.canvas.create_line(0, 150, d, 150)

            if a > 180 or b > 180 or c > 180 or d > 180:
                break
        tkinter.mainloop()









kaas = gui()

