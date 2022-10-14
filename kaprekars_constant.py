# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         DHRUV HALDERIA
# Section:      503
# Assignment:   LAB 7.28
# Date:         13 October 2022
#
#
# got number in 
num = input("Enter a four-digit integer: ")
origNum = int(num)
while len(num) != 4:
    num+= "0"
# this the the iterations variable
iterations  = 0
list = []
#this will get the iterations till 6174
print(origNum, end= " > ")
while num != "6174" and num != "0000":
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
    if int(num) != 6174 and int(num) != 0:
        print(num, end= " > ")
    else:
        print(num)
    while len(num) != 4:
        num+= "0"
print(f"{origNum} reaches {int(num)} via Kaprekar's routine in {iterations} iterations")
