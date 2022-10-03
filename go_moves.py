# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Tilman Strickland
#               Dhruv Halderia
#               Logan Stringer
# Section:      503
# Assignment:   6.12
# Date:         10/3/2022
going = "go"
grid = [[".",".",".",".",".",".",".",".","."], [".",".",".",".",".",".",".",".","."], [".",".",".",".",".",".",".",".","."], [".",".",".",".",".",".",".",".","."], [".",".",".",".",".",".",".",".","."], [".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."], [".",".",".",".",".",".",".",".","."], [".",".",".",".",".",".",".",".","."], [".",".",".",".",".",".",".",".","."]]
while going != "stop":
    grid[ int(float(input("What grid do you want to change? ")))-1][int(float(input("What value within the value? ")))-1] = "x"
    for i in range(len(grid[0])):
        for x in grid[i]:
            print(x, end = " ")
        print()
    going = input('Enter "go" to keep playing, enter "stop" to stop playing ' )