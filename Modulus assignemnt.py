# Exercise:1
import random
import math

# Generate a random number between 1 and 100
number = random.randint(1, 100)

# Calculate square root
square_root = math.sqrt(number)

# Display result
print("Random Number:", number)
print("Square Root:", square_root)

# Exercise 2:
import student

name = input("Enter Name: ")

marks = [20, 56, 89]

average = student.calculate_average(marks)
grade = student.find_grade(average)

student.display_result(name, average, grade)
def calculate_average(marks_list):
    return sum(marks_list) / len(marks_list)

def find_grade(average):
    if average >= 50:
        return "Pass"
    else:
        return "Fail"

def display_result(name, average, grade):
    print("Name:", name)
    print("Average:", average)
    print("Grade:", grade)
