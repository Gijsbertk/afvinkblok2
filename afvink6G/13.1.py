import tkinter
from tkinter import messagebox

class gui:
    def __init__(self):
        self.window =  tkinter.Tk()
        self.boven = tkinter.Frame(self.window)
        self.onder = tkinter.Frame(self.window)
        self.rechts = tkinter.Frame(self.window)
        self.knop1 = tkinter.Button(self.onder, text = 'Show info', command = self.doen )
        self.knop2 = tkinter.Button(self.rechts, text = 'Quit')
        self.waarde = tkinter.StringVar()
        self.waarde_label = tkinter.Label(self.boven, infor=self.waarde)
        self.knop1.pack(side = 'bottom')
        self.knop2.pack(side = 'right')
        self.boven.pack()
        self.onder.pack()
        self.rechts.pack()
        self.waarde_label.pack()
        tkinter.mainloop()

    def doen(self):
        tkinter.messagebox.showinfo('info', 'Gijsbert Keja')

kak = gui()