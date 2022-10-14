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
# got number in 
num = input("Enter a four-digit integer: ")
origNum = int(num)
if len(num) == 3:
    num += "0"
# this the the iterations variable
iterations  = 0
list = []
#this will get the iterations till 6174
while num != "6174":
    list = []
    for i in range(len(num)):
        list.append(num[i:i+1])
    listA = sorted(list)
    listR = sorted(list, reverse = True)
    rNum = ""
    aNum = "" 
    for i in range(len(listA)):
        rNum += listR[i]
        aNum += listA[i]
    num = f"{int(rNum) - int(aNum)}"
    iterations +=1
print(f"{origNum} reaches 6174 via Kaprekar's routine in {iterations} iterations")
