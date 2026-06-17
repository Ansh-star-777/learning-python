from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Event Handler")
window.geometry("400x400")

def msg():
    messagebox.showwarning("Alert","Stop!! Virus detected")

button = Button(master=window,text="Scan for virus",command=msg) 
button.place(x=40,y=40)



window.mainloop()
