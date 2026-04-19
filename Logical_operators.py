a = 0
b = 1
print(type(True))
print(True == 1)
print(False == 0)

# And operator
print(0 and 1)
print(1 and 1)
print(1 and 0)
print(0 and 0)

# Or operator
print("-----------------------------------")
print(1 or 0)
print(1 or 1)
print(0 or 1)
print(0 or 0)

# Not operator (changes value to it's opposite)
print("-----------------------------------")
c = 1

if not c:
    print(True)
else:
    print(False)





user_input = int(input("Enter a number"))
if user_input >= 20 and user_input <= 30:
    print("in range 20 and 30")
else:
    print("not in range")
