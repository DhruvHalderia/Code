# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         DHRUV HALDERIA
# Section:      503
# Assignment:   LAB 6.14
# Date:         3 October 2022
#
# the user inputs the number they want sequenced
initialNum = int(float(input("Enter a positive integer: ")))
iterations = 0
#using a while loop to through the sequences until the inputed number reaches one
print(f"The Juggler sequence starting at {initialNum} is: ")
if initialNum == 1: print(initialNum, end="")
while initialNum != 1:
    if iterations !=0: print(", ",end="") 
    else: print(initialNum, end=", ")
    if initialNum%2 == 0:
        initialNum = int(initialNum**(1/2))
    else:
        initialNum = int(initialNum**(3/2))
    iterations+=1
    print(initialNum, end="")
print()
print(f"It took {iterations} iterations to reach {initialNum} ")