print("          LOOP ASSIGNMENT")
print("      ≈≈Using while loop")
print("Q1")
i = 1
while i <= 100:
  print(i)
  i = i + 1
print("===========================")
print("Q2")
i = 100
while i >=1:
  print(i)
  i=i-1
print("=========================")
print("Q3")
count = 1
table=5
while count<=10:
  print(table*count)
  count= count+1
print("=========================")
print("Q4")
numbers = [12, 45, 8, 23, 67, 34, 90, 15, 56, 78]
i = 0
while i < len(numbers):
  print(numbers[i])
  i = i + 1
print("=========================")
print("Q5")
numbers = (18, 45, 72, 91, 34, 56, 29, 83, 67, 10)
x=67
i = 0
while i < len (numbers):
  if (numbers[i]==x):
    print("Found at index",i)
  i = i + 1
print("=========================")
print("Q6")
sum = 0
i = 1
while i <= 5:
  sum += i
  i += 1
print(sum)
print("==========================")
print("≈≈Using for loop")
print("Q1")

fruits = ['Apple', 'Banana', 'Mango', 'Orange', 'Grapes', 'Peach', 'Cherry', 'Guava',
'Pineapple', 'Watermelon']
for fruit in fruits:
  print(fruits)
print("=========================")
print("Q2")
cities = ('Karachi', 'Lahore', 'Islamabad', 'Peshawar', 'Quetta', 'Multan', 'Hyderabad',
'Faisalabad', 'Sialkot', 'Sukkur')
for city in cities:
  print(cities)
print("=========================")
print("Q3")
numbers= [1,2,3,4,5]
factorial=1
for num in numbers:
  factorial*=num
print(factorial)
print("=========================")
print("≈≈Using range()")
print("Q1")
for num in range(101):
  print(num)
print("=========================")
print("Q2")
for num1 in range(-1,100):
  print(num1)
print("=========================")
print("Q3")
n = 2
for num in range(1,11):
  factorial=n*num
  print(factorial)


