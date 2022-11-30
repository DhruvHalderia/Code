# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Tilman Strickland
#               Dhruv Halderia
#               Logan Stringer
# Section:      503
# Assignment:   Lab 13 Team
# Date:         11/27/2022
import random 
def makeBoard():
#This makes the initial board for the user
    top = [' B'," I"," N"," G"," O"]
    total = [top]
    for i in range(5):
        row =[]
        for b in range(5):
            temp = random.randint(1,99)
            if temp < 10:
                temp = '0'+str(temp)
            row += [temp]
        total += [row]
    total[3][2] = 'xx'  
    printBoard(total)
    return total
def printBoard(x):
    for i in x:
        for b in i:
            print(b, end=' ')
        print()

def getRandomNumbers():
    print()



print("------Welcome to Bingo------\n--------Instructions--------\n----You get a free space----\n---Try to get 5 in a row----\n--Rows can be horizontal,---\n---diagonal, and vertical---\n-----------Enjoy!-----------")
gameBoard = makeBoard()
print()
userInput = int(input("Enter 1 to start the game "))
while userInput == 1: 
    print()