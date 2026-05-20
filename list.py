list_1 = [2000,1999,2008,3033]
list_2 = ["math",84,"science",456,67]

print(len(list_1))
print(len(list_2))
print(list_1)
print(list_1[2])
print(list_1[0],list_1[1])
print(list_2[1:4]) # slicing out

# for list_2 in range(5):
#     print(list_2)

for el in list_2:
    print(el)

list_3 = list_1 + list_2
print(list_3) #concatenation

list_1.extend(list_2)
print(list_1)

doubles = [1,2,4,6,7] * 2
print(doubles)

anything = [10,50,70,80,90]
print(anything[::-1]) # [start:end:step]
print(anything[:])
print(anything[::2])
