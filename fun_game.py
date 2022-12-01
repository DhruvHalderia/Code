# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Tilman Strickland
#               Dhruv Halderia
#               Logan Stringer
# Section:      503
# Assignment:   Lab 13 Team
# Date:         11/30/2022
import random 
import turtle as t
def makeBoard():
    """This makes the initial board for the user using bingo rules and returns the board"""
    top = [' B'," I"," N"," G"," O"]
    total = [top]
    allNums = []
    # The for loop below will make the board with random unique numbers
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
    '''This will print the game board for the player to see'''
    global outputFile
    newString = ''
#the for loops will print out every value on the same line and then add a newline when there is a new row introduced
    for i in x:
        for b in i:
            print(b, end=' ')
            newString+=str(b) 
        newString+="\n"
        print()
    outputFile.write(newString)
    print()

def getRandomNumbers(board):
    '''This gets random rolls from the "pile" and then it calls a function to see if the number is in the board'''
    global usedNums
    global outputFile
    positions = {0:"B", 1: "I", 2: "N", 3:"G", 4:"O"}
    posNum = random.randint(0,4)
    # the if statements down below are used to get random numbers but with the global variable usedNums, they will never repeat a number
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
    '''This gets the input from the user and returns a value to for the variable userInput'''
    # the go variable lets the code know to continue the code or keep repeating itself and the if loop gives two different sets of options
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
    '''This checks the board to see if the number rolled is on the players board'''
    fillerNum = 0
    listRow = 0
    # the for loop check each number in the board and sees if it the number drawed, if it is it'll change it to 'xx'
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
    '''This prints the instructions for player'''
    print("------Welcome to Bingo------\n--------Instructions--------\n----You get a free space----\n---Try to get 5 in a row----\n--Rows can be horizontal,---\n---diagonal, and vertical---\n--And the max number is 75--\n---file records all rolls---\n-----------Enjoy!-----------")

def checkBingo(board):
    '''This will call three other functions and if any of them return true then this will return true'''
    if(checkDiagonal(board)):
        return True
    if (checkVertical(board)):
        return True
    if (checkHorizontal(board)):
        return True
    return False

def checkDiagonal(board):
    '''This will check the diagonal to see if a diagonal bingo is reached'''
    # the two if statements check if there are 'xx' on those positions, if they are, the function returns true
    if(board[1][0] =='xx' and board[2][1] =='xx' and board[3][2] =='xx' and board[4][3] =='xx' and board[5][4] =='xx'):
        return True
    if(board[1][4] =='xx' and board[2][3] =='xx' and board[3][2] =='xx' and board[4][1] =='xx' and board[5][0] =='xx'):
        return True
    return False

def checkVertical(board):
    '''This will check if a vertical bingo is hit'''
    #the for loop will check the columns to see if they are all "xx", if they are the function will return true
    for i in board:
        counter = 0
        for b in i:
            if b =="xx":
                counter+=1
        if counter == 5:
            return True
    return False

def checkHorizontal(board):
    '''This will check if a horizontal bingo is hit'''
    columnChecker = 0
    # the bottom for loops check through the row to see if they are all "xx", if they are the function will return true
    for b in range(5):
        columnChecker = 0
        for i in board:
            if i[b] == "xx":
                columnChecker+=1
        if columnChecker == 5:
            return True
    return False
def drawBingo():
    #we use turtle to draw the word bingo when the user gets a bingo
    t.speed(15)
    t.setup(1920,1080)
    t.penup()
    t.backward(450)
    t.pendown()
    t.pensize(10)
    t.color("Red")
    t.circle(65-1,180)
    t.left(90)
    t.forward(125*2)
    t.left(90)
    t.circle(65-1,180)
    t.penup()

    t.circle(65,180)
    t.forward(250)
    t.left(180)
    t.pendown()
    t.pensize(10)
    t.color('Red')
    t.forward(150)
    t.backward(150)
    t.forward(75)
    t.right(90)
    t.forward(240)
    t.left(90)
    t.forward(75)
    t.backward(150)

    t.penup()
    t.backward(50)
    t.pendown()
    t.left(90)
    t.forward(240)
    t.right(180)
    t.forward(240)
    t.right(145)
    t.forward(280)
    t.left(145)
    t.forward(240)
    t.up()
    
    t.right(90)
    t.forward(160)
    t.left(180)
    t.pendown()
    t.circle(130,180)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.forward(40)
    t.left(180)
    t.forward(90)

    t.penup()
    t.forward(160)
    t.right(90)
    t.forward(45)
    t.left(90)
    t.pendown()
    t.circle(130,360)
    t.Screen().exitonclick()  

getInstructions()
outputFile = open("Bingo_Game.txt",'w' )
gameBoard = makeBoard()
userInput = getInput()
usedNums = []
#this will continue on asking the user to play until they stop or they win with bingo
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
