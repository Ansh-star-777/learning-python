my_dict = {'name': "Ansh", 'age' : 13, 'grade': "special"}
print(my_dict['name'])
print(my_dict['grade'])
print(len(my_dict))
# my_dict.clear()
print(my_dict)
new_dict = my_dict.copy()
new_dict.clear()
print(my_dict,new_dict)
print(my_dict.values(),my_dict.keys())
# print(my_dict['colour'])
print(my_dict.get('colour'))

for my in my_dict:
    print(my_dict[my])

alphabet_dict = {'a':1, 'b':0, 'c':1, 'd':0, 'e':1}
result = 0

for key in alphabet_dict:
    if alphabet_dict[key] == 1:
        result = result + 1
print("The number of times 1 appears in the dictionary is:",result)

country_code_dict = {'India':91, 'NZ':64, 'USA':1 }

country_name = input("Enter a country")
print(country_code_dict.get(country_name))
