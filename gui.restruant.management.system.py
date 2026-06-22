from tkinter import *
from tkinter import ttk,messagebox

class RestruantOrderManagement:
    def __init__(self,window):
        self.window = window
        self.window.title("Res Mang App")
        self.menu_items = {
            "Burger":999,
            "Pizza":1500,
            "Coco Cola":100,
            "Fries":250,
            "Cucumber":1000000
        }
        self.setup_background()
        frame = ttk.Frame(window)
        frame.pack(padx=10,pady=10)
        self.window.geometry("500x500")
        ttk.Label(frame,text="Res Mang App").grid(row=0,columnspan=3,padx=10,pady=10)
        self.menu_labels = {}
        self.menu_quantities = {}

        for i,(item,price) in enumerate(self.menu_items.items(),start=1):
            label = ttk.Label(frame,text=f"{item} (${price}):")
            label.grid(row=i,column=0,padx=10,pady=5)
            self.menu_labels[item] = label

            quantity_entry = ttk.Entry(frame,width=5)
            quantity_entry.grid(row=i,column=1,padx=10,pady=5)
            self.menu_quantities[item] = quantity_entry
        
        ttk.Button(frame,text="Place Order",command=self.place_order).grid(row=len(self.menu_items)+1,column=0,columnspan=2,pady=10)
    
    def setup_background(self):
        self.window.configure(bg="lightblue")
    
    def place_order(self):
        total = 0
        for item,entry in self.menu_quantities.items():
            qty = entry.get()
            if qty.isdigit():
                total = total + int(qty) * self.menu_items[item]
        messagebox.showinfo("Order Total",f"Total Bill: ${total}")


root = Tk()
app = RestruantOrderManagement(root)
root.mainloop()

