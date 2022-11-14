# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         DHRUV HALDERIA
# Section:      503
# Assignment:   LAB 11.12
# Date:         11/14/22
#
#This makes the coins variable and output and user file
coins = 0 
outputFile = open('coins.txt', 'w')
userFile = open('game.txt','r')
#this goes through every line in the code
fileList = []
for i in userFile.readlines():
    fileList.append(i)

parseNum = 0
while parseNum < len(fileList):
#the if statements determine if the coin is valid
    if 'jump' in fileList[parseNum]:
        if '+' in fileList[parseNum]:
            parseNum += int(fileList[parseNum][6:])
        else:
            parseNum -= int(fileList[parseNum][6:])
    elif 'coin' in fileList[parseNum]:
        if '+' in fileList[parseNum]:
            outputFile.write(fileList[parseNum][6:])
            coins+= int(fileList[parseNum][6:])
            parseNum+=1
        else:
            outputFile.write(fileList[parseNum][5:])
            coins-= int(fileList[parseNum][6:])
            parseNum+=1
    else:
        parseNum+=1
    
    
print(f'Total coins collected: {coins}')
userFile.close()
outputFile.close()