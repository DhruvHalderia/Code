# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         DHRUV HALDERIA
# Section:      503
# Assignment:   LAB 4.16
# Date:         18  September 2022
#
#getting all the inputs
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
num3 = float(input("Enter number 3: "))

#using if statements to compare the numbers and find the largest one
if(num1 >= num2 and num1 >= num3):
    print(f"The largest number is {num1:.1f}")
elif(num3 >= num2 and num3 >= num1):
    print(f"The largest number is {num3:.1f}")
elif(num1 <= num2 and num2 >= num3):
    print(f"The largest number is {num2:.1f}")