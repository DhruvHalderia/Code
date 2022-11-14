# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         DHRUV HALDERIA
# Section:      503
# Assignment:   LAB 11.11
# Date:         11/13/22
#
def valid(numList):
    sum1 = 0
    sum2 = 0
    for i in range(0,len(numList)-2,2):
        sum1 += numList[i]
    for i in range(1,len(numList)-1,2):
        sum2 +=numList[i]
    barNum = 3*sum2 + sum1
    LastNum = str(barNum)[-1]
    if numList[-1] == (10-int(LastNum)):
        return True
    return False

#i opened the txt file here
fileName = input("Enter the name of the file: ")
file1 = open(fileName,'r' )
counter = 0 
outputFile = open("valid_barcodes.txt", 'w')
for line in file1.readlines():
    listOfNums =[]
    for i in range(len(line)-1):
        listOfNums.append(int(line[i]))
    if(valid(listOfNums)):
        counter+=1
        outputFile.write(line)
print(f'There are {counter} valid barcodes')
file1.close()
outputFile.close()

    