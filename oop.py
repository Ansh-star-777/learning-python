# class fruit:
    # print("This is an example of a class and an object")

# obj1 = fruit()

class fruit:
    def __init__(self,name,colour):
        self.name = name
        self.colour = colour

apple = fruit("Apple","Red")
print(apple,apple.name,apple.colour)

pineapple = fruit("Pineapple","Yellow")
print(pineapple.name,pineapple.colour)

class student:
    def __init__(self,name,roll_number,school,age):
        self.name = name
        self.roll_number = roll_number
        self.age = age
        self.school = school

ansh = student("Ansh","7","edgewater college","13")
print(ansh.name,ansh.roll_number,ansh.school,ansh.age)

class Vehicle:
    def __init__(self,average,model_name,price,company):
        self.average = average
        self.model_name = model_name
        self.price = price
        self.company = company

buggati = Vehicle("12","Cheron","4-5 mill","Buggati")
print(buggati.average,buggati.model_name,buggati.price,buggati.company)
