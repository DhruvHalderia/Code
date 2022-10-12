# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Tilman Strickland
#               Dhruv Halderia
#               Logan Stringer
# Section:      503
# Assignment:   Lab 7 Team
# Date:         10/3/2022
going = "go"
# the code below is instantiating the initial grid
grid = [[" ",1,2,3,4,5,6,7,8,9],["1",".",".",".",".",".",".",".",".","."], ["2",".",".",".",".",".",".",".",".","."], ["3",".",".",".",".",".",".",".",".","."], ["4",".",".",".",".",".",".",".",".","."], ["5",".",".",".",".",".",".",".",".","."], ["6",".",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".",".","."], ["8",".",".",".",".",".",".",".",".","."], ["9",".",".",".",".",".",".",".",".","."]]
#this is so if the user doesn't want to play the game anymore they can say stop and the program would stop
while going != "stop":
#this will print the grid
    for i in range(len(grid[0])):
       for x in grid[i]:
           print(x, end = " ")
       print()
    #this gets the grid position that player one wants to put a stone at 
    gridVal = int(float(input("What grid do you want to change player one? ")))
    placeVal = int(float(input("What value within the grid player one? ")))
    #this detects if there is a stone at that position already 
    if(grid[gridVal][placeVal] != "."):
        while(grid[gridVal][placeVal] != "."):
            print("This spot is already taken, please enter a new spot down below")
            gridVal = int(float(input("What grid do you want to change player one? ")))
            placeVal = int(float(input("What value within the grid player one? ")))
            print()
    #below the grid changes the value the player wants to put their stone at 
    grid[gridVal][placeVal] = chr(9675)
    #this will print the grid with the stone placed there 
    for i in range(len(grid[0])):
        for x in grid[i]:
            print(x, end = " ")
        print()
    #this gets the grid position that player two wants to put a stone at 
    gridVal = int(float(input("What grid do you want to change player two? ")))
    placeVal = int(float(input("What value within the grid player two? ")))
    #this detects if there is a stone at that position already 
    if(grid[gridVal][placeVal] != "."):
        while(grid[gridVal][placeVal] != "."):
            print("This spot is already taken, please enter a new spot down below")
            gridVal = int(float(input("What grid do you want to change player two? ")))
            placeVal = int(float(input("What value within the grid player two? ")))
            print()
    #below the grid changes the value the player wants to put their stone at
    grid[gridVal][placeVal] = chr(9679)
    #this will print the grid with the stone placed there 
    for i in range(len(grid[0])):
        for x in grid[i]:
            print(x, end = " ")
        print()
    #this asks the user if they want to continue or stop playing the game
    going = input('Enter "go" to keep playing, enter "stop" to stop playing ' ).replace(" ", "")
print("\nThanks for playing!")
print()