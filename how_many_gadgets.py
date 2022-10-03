# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         DHRUV HALDERIA
# Section:      503
# Assignment:   LAB 4.18
# Date:         19 September 2022
#
# below I get the days
day = int(float(input("Please enter a positive value for day: ")))
# I made if statements to calculate the amount of toys made
if(day <= 0):
    print("You entered an invalid number!")
if(day > 0 and day <= 10 ):
    print(f"The total number of gadgets produced on day {day} is {day * 5}")
if(day > 10 and day <= 60):
    print(f"The total number of gadgets produced on day {day} is {50 + ((day - 10) * 50)}")
if(day > 60):
    daySixty = 2550
    leftDay = day - 60
    gadgets = 50 - leftDay
    if(day == 61):
        print(f"The total number of gadgets produced on day {day} is {daySixty + (49)}")
    elif(day < 101):
        print(f"The total number of gadgets produced on day {day} is {int(daySixty+((49 + gadgets)/2) * leftDay)}")
    else:
        print(f"The total number of gadgets produced on day {day} is {3730}")

