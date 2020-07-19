# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 13:34:43 2020

@author: Eriel
"""


from tkinter import *

from PIL import Image, ImageTk

menu = Tk() # New window named menu 
menu.geometry('500x500') # window size
menu.title("menu")
menu.iconbitmap(r'graphy.ico')
menu['bg'] = '#161616'


canvas = Canvas(menu, height = 244, width = 365, bg = '#161616' )
canvas.pack(pady= 10)
wel_img = PhotoImage(file='welcome.png')
canvas.create_image(0, 0, anchor = NW,  image = wel_img)

text = Label (menu, text = 'Hello', bg = '#161616')
text.pack()

# Menu
menu_frame = Frame(menu, bg = '#161616')
menu_frame.pack()

def play_btn():
        print("Hello World!!!")
        
graph_btn = PhotoImage(file = r"graph_btn.png")
exit_btn = PhotoImage(file = r"exit_btn.png")
btn = Button(menu_frame, image = graph_btn, command = play_btn(), bg = '#161616')
btn.pack(pady = 10)
btn = Button(menu_frame, image = exit_btn, command = play_btn(), bg = '#161616')
btn.pack(pady = 10)


menu.mainloop() # Runs menu in a loop