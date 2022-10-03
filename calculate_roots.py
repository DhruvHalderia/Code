# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         DHRUV HALDERIA
# Section:      503
# Assignment:   LAB 4.19
# Date:         19 September 2022
#
from math import *
a = int(float(input("Please enter the coefficient A: ")))
b = int(float(input("Please enter the coefficient B: ")))
c = int(float(input("Please enter the coefficient C: ")))
# this evaluates if there is a valid number of coefficients
if(a == 0 and b == 0):
    print("You entered an invalid combination of coefficients!")
elif(a > 0 ):
    rootOne = (-b/(2*a))
    posOrNeg = False
# This calculates if there is going to be an imaginary number in the equation
    if (((b ** 2) - (4 * a * c)) / (2 * a) < 0):
        rootTwo = int((sqrt(abs(((b**2)-(4*a*c))/(2*a)))))
        posOrNeg = True
    else:
        rootTwo = (sqrt((b ** 2) - (4 * a * c)) / (2 * a))
# This displays the final roots
    if(posOrNeg):
        print(f'The roots are x = {rootOne} + {rootTwo:.1f}i and x = {rootOne} - {rootTwo:.1f}i')
    else:
        if(rootTwo != 0):
            print(f'The roots are x = {rootOne + rootTwo} and x = {rootOne - rootTwo}')
        else:
            print(f'The root is x = {rootOne + rootTwo}')

else:
#this calculates the root with out an a coefficient
    print(f'The root is x = {(-c)/b}')




