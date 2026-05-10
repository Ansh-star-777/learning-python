for i in range(8):
    if i == 5:
        continue
    print(i)

print()

print("------------------")

for i in range(8):
    if i == 5:
        pass
    print(i)

print()

print("-------------------")

for i in range(8):
    if i == 5:
        break
    print(i)

print()

print("-------------------")

a = input("enter a word")

while a != "exit":
    a = input("enter a word")


while True:
    a = int(input("enter a number"))
    if a == 5:
        break
    else:
        print(a)
