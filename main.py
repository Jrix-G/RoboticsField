from tkinter import *
import os

main = Tk()
main.title("Fish")
hauteur = 1000
largeur = 1000
main.maxsize(height=hauteur, width=largeur)
main.minsize(height=hauteur, width=largeur)

canvas = Canvas(main, width=largeur, height=hauteur, background='white')
canvas.pack(fill="both", expand=True)

main.mainloop()