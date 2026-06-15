from tkinter import *

window = Tk()
window.title("Login app")
window.geometry("400x400")

f1 = Frame(master=window,height=200,width=360,bg="blue")

l1 = Label(master=f1,text="Full Name:",bg="#3895D3",fg="white",width=12)
l2 = Label(master=f1,text="Email:",bg="#3895D3",fg="white",width=12)
l3 = Label(master=f1,text="Password:",bg="#3895D3",fg="white",width=12)

name_entry = Entry(f1)
email_entry = Entry(f1)
password_entry = Entry(f1,show="*")
