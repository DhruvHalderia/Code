# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         DHRUV HALDERIA
# Section:      503
# Assignment:   LAB 6.13
# Date:         3 October 2022
#
#got the integers from the user
int1  = int(float(input("Enter an integer: ")))
int2  = int(float(input("Enter another integer: ")))
#used a for loop to go through 1 - 100 and if statements to see if they are divisable
for i in range(100):
        if (((i+1) % int1 == 0) and ((i+1) % int2 == 0)):
            print("Howdy Whoop")
        elif (i+1) % int1 == 0:
            print("Howdy")
        elif (i+1) % int2 == 0:
            print("Whoop")
        else:
            print(i+1)