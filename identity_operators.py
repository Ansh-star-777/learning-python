a = [1,2,3,4,5]
b = [1,2,3,4,5]
c = a

print(a is c) # True
print(a is b) # True -> False (correct)
print(a is not c) # False
print(a is not b) # False -> True (correct)



print("--------------------------------------")

# Membership operators
print(a in c)
print(a not in b)
print(c in a)

message = "Hello world"
print("Hello" in message)
print(1 in a)
print(6 not in a)

print("-----------------------------------------------")

x = 5.67

if type(x) is int:
    print("Type is int")
else:
    print("Not int")

email_address = "ansh@gmail.com"

if "gmail" in email_address:
    print("used gmail")
else:
    print("Not gmail")
