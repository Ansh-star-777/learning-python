from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename

window = Tk()
window.title("Text")
window.geometry("700x700")

def open_file():
    file_path = askopenfilename(filetypes=[("Text Files","*.txt")])
    if not file_path:
        return
    with open(file_path,"r") as file:
        content = file.read()
    text_area.delete("1.0",END)
    text_area.insert(END,content)

button_frame = Frame(window)
button_frame.pack(fill=X)

open_button = Button(button_frame,text="Open",command=open_file)
open_button.pack(side=LEFT,padx=5,pady=5)
# save_button = Button(button_frame,text="Save",command=save_file)
# save_button.pack(side=LEFT,padx=5,pady=5)

text_area = Text(window)
text_area.pack(expand=True)



window.mainloop()
