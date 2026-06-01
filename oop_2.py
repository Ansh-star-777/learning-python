class fruit:
    def __init__(self,name,colour):
        self.name = name
        self.colour = colour
    def __del__(self):
        print("Object has been destroyed")
    def intro(self):
        print("My name is",self.name,"and my colour is",self.colour)

fruit_1 = fruit("Watermelon","Green")
# print(fruit_1.name,fruit_1.colour)
fruit_1.intro()
del fruit_1
# print(fruit_1)

print("-__-,:D,^_^")

class Cars:
    def __init__(self,name,colour,price):
        self.name = name
        self.colour = colour
        self.price = price
    def engine(self):
        print("Engine has been started",self.name)
    def __del__(self):
        print("Deleted")

konikeseg = Cars("Jesko","All black","You can't afford it!!")
print(konikeseg.colour,konikeseg.price)
konikeseg.engine()
del konikeseg

class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def withdraw(self,withdraw_balance):
        self.balance = self.balance - withdraw_balance

ansh_account = BankAccount("Ansh",10000)
print("current balance:",ansh_account.balance)
ansh_account.withdraw(2000)
print("new balance:",ansh_account.balance)
