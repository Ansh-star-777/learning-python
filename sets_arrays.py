import array as arr

my_set = {9,1,1,2,2,2,3,4,5,5}
another_set = {5,6,7}
print(my_set)
my_set.add(9)
print(my_set)
result = my_set & another_set
print(result)

res = my_set.intersection(another_set)
print(res)

result_1 = my_set.union(another_set)
print(result_1)

result_5 = my_set.difference(another_set)
print(result_5)

a = arr.array('i',[4,5,6])
print(a)

for element in a:
    print(element)

print(a[2])

another_set.pop()
print(another_set)
