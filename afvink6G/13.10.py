import tkinter
import tkinter.font

class gui:
    def __init__(self):
        self.window = tkinter.Tk()
        self.midden = tkinter.Frame()

        self.canvas = tkinter.Canvas(self.window, width=200, height=200)
        self.canvas.create_line(0, 100, 80, 100)
        self.canvas.create_line(0, 100, 80, 150)
        self.canvas.create_line(80, 150, 80, 200)
        self.canvas.create_line(80, 200, 110, 160)
        self.canvas.create_line(110, 160, 150, 200)
        self.canvas.create_line(150, 200, 150, 150)
        self.canvas.create_line(150, 150, 200, 100)
        self.canvas.create_line(200, 100, 130, 100)
        self.canvas.create_line(130, 100, 105, 20)
        self.canvas.create_line(105, 20, 80, 100)
        self.canvas.create_text(110, 120, text='Gijsbert')



        self.canvas.pack()
        self.midden.pack()
        tkinter.mainloop()

GUI = gui()