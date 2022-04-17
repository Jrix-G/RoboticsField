#EasySnake made by Jason

#
# ---- En cours de développement ----
#

from tkinter import *
from random import *
from time import *

window = Tk()
window.title("EasySnake")
window.minsize(700, 700)
window.maxsize(700, 700)

canvas = Canvas(window, width=700, height=700)
canvas.pack()

class homme():
    def __init__(self, x, y, width, height):
        self.name = canvas.create_rectangle(x, y, width+x, height+y, fill="red")
        self.largeur = width
        self.hauteur = height
        self.x = x
        self.y = y
    def move_right(self):
        canvas.delete(self.name)
        self.name = canvas.create_rectangle(self.x, self.y, self.largeur+self.x, self.hauteur+self.y, fill="red")
        self.x = self.x+10
    def move_left(self):
        canvas.delete(self.name)
        self.name = canvas.create_rectangle(self.x, self.y, self.largeur+self.x, self.hauteur+self.y, fill="red")
        self.x = self.x-10
    def move_up(self):
        canvas.delete(self.name)
        self.name = canvas.create_rectangle(self.x, self.y, self.largeur+self.x, self.hauteur+self.y, fill="red")
        self.y = self.y-10
    def move_down(self):
        canvas.delete(self.name)
        self.name = canvas.create_rectangle(self.x, self.y, self.largeur+self.x, self.hauteur+self.y, fill="red")
        self.y = self.y+10

    def getname(self):
        return self.name

homme2 = homme(10, 10, 10, 10) 
homme = homme(10, 10, 10, 10)
 
i = 0

def Run():
    global i 
    window.after(50, Run)
    homme.move_right()
    if i >= 20:
        homme2.move_right()
    else:
        homme2.move_down()
    i+= 1
    
window.after(1, Run)
run = True
window.mainloop()