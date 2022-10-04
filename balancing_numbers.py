# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         DHRUV HALDERIA
# Section:      503
# Assignment:   LAB 6.15
# Date:         3 October 2022
#
# gets user input
userInput = int(float(input("Enter a value for n: ")))
sum = 0 
# goes through the numbers and gets the sum
for i in range(userInput-1):
    sum += i+1
balNum = 0 
r = 0
tempInput = userInput
#gets the balance numbers
while(balNum < sum):
    r+=1
    balNum += tempInput+1
    tempInput+=1
#sees if the number is a balance number
if balNum == sum:
    print(f"{userInput} is a balancing number with r={r}")
else:
    print(f"{userInput} is not a balancing number")