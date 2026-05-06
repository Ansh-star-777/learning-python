a = 2
b = 5

def add_numbers(a,b):
    print("Adding.......")
    print("Result:",a + b)

add_numbers(a,b)

print("-----------------------")

m = int(input("enter a num"))
n = int(input("enter a num"))
p = int(input("enter a num"))

def multipication_numbers(m,n,p):
    print("we are still doing it.....")
    print("i got it:",m * n * p)

#multipication_numbers(m,n,p)

print("------------------------------------------")

def calculator_num(a,b):
    operation = input("which one do you want bro = + - * /")
    a = int(input("enter the first num"))
    b = int(input("enter the second num"))
    if operation == "+":
        print("result is perfecto",a + b)
    
calculator_num(a,b)
