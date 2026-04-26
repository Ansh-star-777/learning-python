message = "ansh maan"

for i in message:
  print("The value of i is:",i) 

for i in range(11):
  print(i)
  
  range_input = input("Enter number you want to sum until")
sum = 0

for i in range(range_input):
  sum = sum + i

print("Result:",sum)
