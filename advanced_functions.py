numbers = [1,2,3,4,5,6,7]
even = [x for x in numbers if x % 2 == 0]
print(even)

str_dict = {str(x): x**2 for x in [1,2,3,4]}
print(str_dict)


def square_calculator(a):
    return a**2
result = map(square_calculator,numbers)
print(result)
print(list(result))

name = ["ansh","anshika","anshu"]
roll_number = [1,2,3]
zipped = zip(name,roll_number)
print(list(zipped))

ages = [19,22,67,54,45,13,55,65]
for x in ages:
    if x < 18:
        print(x,"not allowed")
        exit()
    else:
        print(x,"allowed")
