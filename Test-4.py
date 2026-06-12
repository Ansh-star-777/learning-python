class Book:
  def __init__(self,title,author):
    self.is_borrowed = False
    self.title = title
    self.author = author
  def borrow(self):
    self.is_borrowed = True
    print("Your book has been borrowed")
  def return_book(self):
    self.is_borrowed = False
    print("Your book has been returned")
  
book_1 = Book("Aura","ANSH")
book_1.borrow()
book_1.return_book()

book_2 = Book("Aura-2","Ansh-2")
book_2.borrow()
book_2.return_book()

book_3 = Book("Aura-3","Ansh-3")
book_3.borrow()
book_3.return_book()
