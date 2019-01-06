from tkinter import *

canvas_width = 600
canvas_height = 600

master = Tk()

w = Canvas(master, width=canvas_width, height=canvas_height)

w.pack()

oval = w.create_oval(75, 75, 500, 500)
minline = w.create_line(150, 150, 300, 300)

mainloop()
