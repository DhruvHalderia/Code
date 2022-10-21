# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Tilman Strickland
#               Dhruv Halderia
#               Logan Stringer
# Section:      503
# Assignment:   8.10 
# Date:         10/21/2022
#time = input("Enter the time: ")
#we get the input from the user with the time variable
time = input("Enter the time: ")
#we get the 
numbers = {"0":["000","0 0","0 0","0 0","000"],"1": [" 1 ", "11 ", " 1 ", " 1 ", "111"], "2": ["222", "  2", "222", "2  ", "222"], "3":["333", "  3", "333", "  3", "333"] ,"4": ["4 4", "4 4","444","  4","  4"], "5": ["555", "5  ", "555", "  5", "555"], "6": ["666","6  ","666","6 6","666"], "7": ["777","  7","  7","  7","  7"],"8":["888", "8 8","888","8 8","888"], "9":["999","9 9","999","  9","  9"], ":": ["   "," : ","   "," : ","   "]}
for i in range(5):
    if len(time) == 5:
        print(numbers[time[0:1]][i],"",numbers[time[1:2]][i],"",numbers[time[2:3]][i],"",numbers[time[3:4]][i],"",numbers[time[4:5]][i])
    else:
        print(numbers[time[0:1]][i],"",numbers[time[1:2]][i],"",numbers[time[2:3]][i],"",numbers[time[3:4]][i])