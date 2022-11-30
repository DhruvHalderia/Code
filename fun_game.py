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
import turtle
def makeBoard():
#This makes the initial board for the user
    top = [' B'," I"," N"," G"," O"]
    total = [top]
    allNums = []
    for i in range(5):
        row =[]
        for b in range(5):
            if b == 0: 
                randBoardNum = random.randint(1,15)
                while randBoardNum in allNums:
                    randBoardNum = random.randint(1,15)   
            elif b == 1:
                randBoardNum = random.randint(16,30)
                while randBoardNum in allNums:
                    randBoardNum = random.randint(16,30)   
                     
            elif b==2:
                randBoardNum = random.randint(31,45)
                while randBoardNum in allNums:
                    randBoardNum = random.randint(31,45)
                    
            elif b== 3:
                randBoardNum = random.randint(46,60)
                while randBoardNum in allNums:
                    randBoardNum = random.randint(46,60)
                    
            else:
                randBoardNum = random.randint(61,75)
                while randBoardNum in allNums:
                    randBoardNum = random.randint(61,75)
            allNums+=[randBoardNum]
            if randBoardNum < 10:
                randBoardNum = '0'+str(randBoardNum)
            row += [randBoardNum]
        total += [row]
    total[3][2] = 'xx'  
    printBoard(total)
    return total

def printBoard(x):
    global outputFile
    newString = ''
    for i in x:
        for b in i:
            print(b, end=' ')
            newString+=str(b) 
        newString+="\n"
        print()
    outputFile.write(newString)
    print()

def getRandomNumbers(board):
    global usedNums
    global outputFile
    positions = {0:"B", 1: "I", 2: "N", 3:"G", 4:"O"}
    posNum = random.randint(0,4)
    if posNum== 0:
        randNumRolled = random.randint(1,15)
        while randNumRolled in usedNums:
            randNumRolled = random.randint(1,15)    
    elif posNum == 1:
        randNumRolled = random.randint(16,30)
        while randNumRolled in usedNums:
            randNumRolled = random.randint(16,30)
    elif posNum==2:
        randNumRolled = random.randint(31,45)
        while randNumRolled in usedNums:
            randNumRolled = random.randint(31,45)
    elif posNum== 3:
        randNumRolled = random.randint(46,60)
        while randNumRolled in usedNums:
            randNumRolled = random.randint(46,60)
    else:
        randNumRolled = random.randint(61,75)
        while randNumRolled in usedNums:
            randNumRolled = random.randint(61,75)
    usedNums+=[randNumRolled]
    ansString = f"\nThe number rolled is: {positions[posNum]}{randNumRolled}"
    print(ansString)
    outputFile.write(ansString+'\n')
    newBoard = checkBoard(board,posNum, randNumRolled)
    return newBoard

def getInput(num = 1):
    go = False
    if num ==1:
        while not go:
            try: 
                userNum = float(input("Enter 1 to roll: "))
                if userNum == 1:
                    go = True
                else:
                    print("Bad input!")
            except:
                print("Bad input!")
    else:
        while not go:
            try: 
                userNum = float(input("Enter 1 to roll, 2 to view instructions, and 3 to exit: "))
                if userNum == 1 or userNum ==2 or userNum == 3:
                    go = True
                else:
                    print("Bad input!")
            except:
                print("Bad input!")
    return userNum

def checkBoard(board, column, number):
    fillerNum = 0
    listRow = 0
    for i in board:
        for b in i:
            try:
                if int(b) == number:
                    board[listRow][column] = "xx"
            except:
                fillerNum+=1
        listRow+=1  
    return board

def getInstructions():
    print("------Welcome to Bingo------\n--------Instructions--------\n----You get a free space----\n---Try to get 5 in a row----\n--Rows can be horizontal,---\n---diagonal, and vertical---\n--And the max number is 75--\n---file records all rolls---\n-----------Enjoy!-----------")

def checkBingo(board):
    if(checkDiagonal(board)):
        return True
    if (checkVertical(board)):
        return True
    if (checkHorizontal(board)):
        return True
    return False

def checkDiagonal(board):
    if(board[1][0] =='xx' and board[2][1] =='xx' and board[3][2] =='xx' and board[4][3] =='xx' and board[5][4] =='xx'):
        return True
    if(board[1][4] =='xx' and board[2][3] =='xx' and board[3][2] =='xx' and board[4][1] =='xx' and board[5][0] =='xx'):
        return True
    return False

def checkVertical(board):
    for i in board:
        counter = 0
        for b in i:
            if b =="xx":
                counter+=1
        if counter == 5:
            return True
    return False

def checkHorizontal(board):
    columnChecker = 0
    for b in range(5):
        columnChecker = 0
        for i in board:
            if i[b] == "xx":
                columnChecker+=1
        if columnChecker == 5:
            return True
    return False
def drawBingo():
    print()



getInstructions()
outputFile = open("Bingo_Game.txt",'w' )
gameBoard = makeBoard()
userInput = getInput()
usedNums = []
while userInput == 1 or userInput == 2: 
    if userInput == 1:
        gameBoard = getRandomNumbers(gameBoard)
        printBoard(gameBoard)
        outputFile.write('\n')
    elif userInput == 2:
        getInstructions()
        printBoard(gameBoard)
    if(checkBingo(gameBoard)):
        outputFile.write("BINGO!")
        userInput = 3
        drawBingo()
    else:
        userInput = getInput(2)
print("Thanks for playing!")
outputFile.close()