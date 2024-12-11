from tkinter import *
import tkinter as ttk
import pyttsx3
RObot=pyttsx3.init()

def func1():
    soundread=Text.get()
    RObot.say(soundread)
    RObot.runAndWait()

def clearTextBox():
    Text.delete(0, END)

form= Tk()
form.geometry('500x600')
form.title('GUI')
form.config(bg="#f9ebe7")

label1=Label(form,text="Converting Text into Audio", font="System 20 bold")
label1.pack(pady=20)

label2=Label(form,text="Enter your text", font="System 20 bold")
label2.pack(pady=10)

Text=ttk.Entry(form,width=60)
Text.pack(pady=10)
Text.config(bg="#FFDFD6")

buttonFrame = Frame(form) 
buttonFrame.pack(pady=10)

button1=ttk.Button(buttonFrame,text='Play',bg="#694F8E",command=func1,width=15,font="System")
button1.grid(row=0, column=0, padx=5)

button2=ttk.Button(buttonFrame,text='Exit',bg="#B692C2",command=exit,width=15,font="System")
button2.grid(row=0, column=1, padx=5)

button3=ttk.Button(buttonFrame,text='Set',bg="#E3A5C7",command=clearTextBox,width=15,font="System")
button3.grid(row=0, column=2, padx=5)

form.mainloop()
