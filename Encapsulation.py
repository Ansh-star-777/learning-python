class BankAcc:
    def __init__(self,name,bank_balance):
        self.name = name
        self.bank_balance = bank_balance

ansh_acc = BankAcc("Ansh",1000000000)
ansh_acc.name = "Ayush"
print(ansh_acc.name,ansh_acc.bank_balance)





# class BankAcc:
#     def __init__(self,name,bank_balance):
#         self.name = name
#         self.__bank_balance = bank_balance
#     def __calculate_interest(self):
#         print("interest")

# ansh_acc = BankAcc("Ansh",1000000000)
# print(ansh_acc.name)
# ansh_acc.__calculate_interest()
# print(ansh_acc.__bank_balance)

class Computer:
    def __init__(self):
        self.__max_price = 101010
    def sell(self):
        print("Selling price:",self.__max_price)
    def set_selling_price(self,price):
        self.__max_price = price

c = Computer()
# print(c.__max_price)
c.sell()
c.set_selling_price(100100100)
c.sell()
