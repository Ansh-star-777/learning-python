from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

window = Tk()
window.title("Denomination Caculator")
window.geometry("700x500")
window.configure(bg="light blue")

upload = Image.open("download.jpg")
upload = upload.resize((500,300))
image = ImageTk.PhotoImage(upload)

label = Label(window,image=image,bg="light blue")
label.pack()

l1 = Label(window,text="Hi User! Welcome To Denomination Counter Application")
l1.pack()

def msg():
    msgbox = messagebox.showinfo("Alert","Do You Want To Calculate The Denomination Count?")
    if msgbox == "ok":
        topwin()

b1 = Button(window,text="Let's Get started",command=msg)
b1.pack()

window.mainloop()
