tuple_number = (1,2,3,5,5,6,7)
tuple_string = ("hi","hello","ansh","ayush")
print(tuple_number,tuple_string)

print(tuple_string[2])

for x in tuple_string:
    print(x)

for x in range(4):
    print(tuple_string[x])

print(tuple_string[1:4])
print(tuple_number.count(10))

weather = (0,1,0,0,1,1,0)
sunny = 0
rainy = 0

for i in range(7):
    if weather[i] == 0:
        sunny = sunny + 1
    else:
        rainy = rainy + 1
if sunny > rainy:
    print("The weather is sunny")
else:
    print("The weather is rainy")
    
