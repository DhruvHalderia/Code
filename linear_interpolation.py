# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Names:        Zachary Earnest
#               Chris Gonzalez
#               Dhruv Halderia
#               Bryce Brumley
# Section:      102 - 503
# Assignment:   Lab 2.8
# Date:         31/08/2022
from math import*
# This calculates the total distance for 25 minutes
time = 25
position = (1400/3)*(time-10) + 2026
print("Part 1:")
print("For t =",time,"minutes, the position p =",position,"kilometers")
#This is calculating the distance from houston
# part 2 starts
time = 300
position = (1400/3)*(time-10) + 2026
circumference = pi *2* (6745)
print("Part 2:")
print("For t =",time,"minutes, the position p =",position % circumference ,"kilometers")
#