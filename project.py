import tkinter as tk
from tkinter import Entry, Frame, Label, filedialog, Text
import os
from tkinter.constants import END

root = tk.Tk()

canvas = tk.Canvas(root, height=700, width=700, bg="#0C2D48")

canvas.pack()

frame = tk.Frame(root, bg="#0C2D48")
frame.place(relwidth=0.8, relheight=.2, relx=0.1, rely= .3)
e = Entry(frame, width =50 ,bg="#FFB52E", fg = "white", borderwidth= 2, font=("Helvetica, 24"))
e.pack()
e.insert(0,"Enter course")

e2 = Entry(frame, width =50 ,bg="#75E6DA", fg = "white", borderwidth= 2, font=("Helvetica, 24"))
e2.pack()
e2.insert(0,"Enter course hours")

def click():
    course = e.get() + " - " + e2.get() + " hours"
    mylabel = Label(root,text= course)
    mylabel.pack()
    e.delete(0,END)
    e2.delete(0,END)
    #changes made
    #another change
def submit():
    mylabel = print("all courses sumbitted")
    mylabel.pack()

addCourse = tk.Button(frame, text="Add course", padx=10, pady=5, 
                    fg="white", bg="#75E6DA", command=click)
submit = tk.Button(frame, text="Submit", padx=21, pady=5 , 
                    fg="white", bg="#75E6DA", command=submit)
def thing():
    print("This works")

addCourse.pack()
submit.pack()

root.mainloop()