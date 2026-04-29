i = 1

while(i <= 5):
    j = 1
    while(j <= 10):
        print(j,end=" ")
        j = j + 1
    print()
    i = i + 1

print("-------------------------------")

a = 1

while(a <= 3):
    b = 50
    while(b <= 70):
        print(b,end=" ")
        b = b + 1
    print()
    a = a + 1


word = input("Enter a word")
letter = input("Enter the letter you want to count the frequancy for??")
i = 0
frequancy = 0

while(i < len(word)):
    if word[i] == letter:
        frequancy = frequancy + 1
    i = i + 1
print("frequancy:",frequancy)
