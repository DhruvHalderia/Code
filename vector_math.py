# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         DHRUV HALDERIA
# Section:      503
# Assignment:   LAB 7.27
# Date:         13 October 2022
#
#
import math
from operator import sub
#below i get the elements from the user and putting into two lists
numA = input("Enter the elements for vector A: ")
numB = input("Enter the elements for vector B: ")
vecA = numA.split()
vecB = numB.split()
magNumA = 0
#gets the magnitude for both vectors
for i in vecA:
    magNumA += float(i)**2
magNumA = math.sqrt(magNumA)
magNumB = 0
for i in vecB:
    magNumB+= float(i)**2
magNumB = math.sqrt(magNumB)
print(f"The magnitude of vector A is {magNumA:.5f}")
print(f"The magnitude of vector B is {magNumB:.5f}")
additionVec = []
subtractionVec = []
dotProduct = 0
#gets the vector addition vector subtraction and dot product
for i in range(len(vecA)):
    additionVec.append(float(vecA[i]) + float(vecB[i]))
    subtractionVec.append(float(vecA[i]) - float(vecB[i]))
    dotProduct += float(vecA[i]) * float(vecB[i])
print("A + B is",additionVec)
print("A - B is",subtractionVec)
print(f"The dot product is {dotProduct:.2f}")

