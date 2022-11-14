# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         DHRUV HALDERIA
# Section:      503
# Assignment:   LAB 11.12
# Date:         11/13/22
#
#This makes the coins variable and output and user file
coins = 0 
outputFile = open('coins.txt', 'w')
userFile = open('game.txt','r')
#this goes through every line in the code
for i in userFile.readlines():
    listOfCoins = i.split(' ')
#the if statements determine if the coin is valid
    if listOfCoins[0]=='coin' or listOfCoins[0] == 'jump':
        if listOfCoins[1][0:2] != '+0':
            coins+=1
            if listOfCoins[1][0] == '+':
                outputFile.write(listOfCoins[1][1:])
            else: 
                outputFile.write(listOfCoins[1])
print(f'Total coins collected: {coins}')
userFile.close()
outputFile.close()