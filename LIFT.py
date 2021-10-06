import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import Button, Frame, Label, Scrollbar, StringVar, ttk
from tkinter import Entry, filedialog, Text
from tkinter.constants import VERTICAL, X
import time
import datetime




root = tk.Tk()
root.title("Project")
root.geometry("1000x900")
root.resizable(0, 0)
root.config(bg = "#0C2D48")


sec = StringVar()
Entry(root, textvariable=sec, width = 2, font = 'Helvetica 14').place(x=600, y=700)
sec.set('00')
mins= StringVar()
Entry(root, textvariable = mins, width =2, font = 'Helvetica 14').place(x=550, y=700)
mins.set('00')
hrs= StringVar()
Entry(root, textvariable = hrs, width =2, font = 'Helvetica 14').place(x=500, y=700)
hrs.set('00')
#Define the function for the timer
def countdowntimer():
   times = int(hrs.get())*3600+ int(mins.get())*60 + int(sec.get())
   while times > -1:
      minute,second = (times // 60 , times % 60)
      hour =0
      if minute > 60:
         hour , minute = (minute // 60 , minute % 60)
      sec.set(second)
      mins.set(minute)
      hrs.set(hour)
      #Update the time
      root.update()
      time.sleep(1)
      if(times == 0):
         sec.set('00')
         mins.set('00')
         hrs.set('00')
      times -= 1
Label(root, font= ('Comic Sans MS','14', 'bold'), text = 'Timer',fg = "black",  bg = "#FFB52E",).place(x=530,y=640)

def clicked():
    box1.configure(text = 'I just got clicked')
btn = Button(
    root,
    text = 'Start',
    bg = "#FFB52E",
    fg = 'Black',
    font= ('Comic Sans MS','14', 'bold'),
     command = countdowntimer
)
btn.grid(
    column= 0,
    row=3,
    pady=25,
    ipadx=10,
    ipady=10
)


box1 = tk.Label(
    root,
    text = "Class List",
    bg = "#FFB52E",
    font= ('Comic Sans MS','14', 'bold'),
    fg = "black"
)
box1.grid(
    column=0,
    row=0,
    sticky=tk.W,
    padx=45,
    pady=30,
    ipadx=40,
    ipady=40
    
)

box2 = tk.Label(
    root,
    text='Input from User',
    bg='#FFB52E',
    font= ('Comic Sans MS','14', 'bold'),
    fg='black'
)
box2.grid(
    column=0,
    row=1,
    sticky=tk.W,
    padx=40,
    pady=10,
    ipadx=35,
    ipady=200
)

box3 = tk.Label(
    root,
    text="Today's View",
    bg='#FFB52E',
    font= ('Comic Sans MS','14', 'bold'),
    fg='black'
)
box3.grid(
    column=1,
    row=0,
    sticky=tk.N,
    padx=45,
    pady=30,
    ipadx=40,
    ipady=40
)
box4 = tk.Label(
    root,
    text='Input from User',
    bg='#FFB52E',
    font= ('Comic Sans MS','14', 'bold'),
    fg='black'
)
box4.grid(
    column=1,
    row=1,
    sticky=tk.N,
    padx=10,
    pady=10,
    ipadx=35,
    ipady=200
)

box5 = tk.Label(
    root,
    text='Completed',
    bg='#FFB52E',
    font= ('Comic Sans MS','14', 'bold'),
    fg='black'
)
box5.grid(
    column=2,
    row=0,
    sticky=tk.E,
    padx=45,
    pady=30,
    ipadx=40,
    ipady=40
)

box6 = tk.Label(
    root,
    text='Input from User',
    bg='#FFB52E',
    font= ('Comic Sans MS','14', 'bold'),
    fg='black'
)
box6.grid(
    column=2,
    row=1,
    sticky=tk.E,
    padx=40,
    pady=10,
    ipadx=35,
    ipady=200
)




root.mainloop()