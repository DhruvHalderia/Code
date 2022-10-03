# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         DHRUV HALDERIA
# Section:      503
# Assignment:   LAB 3.18
# Date:         15 September 2022
#
from math import *
def printresult(shape, side, area):
    '''Print the result of the calculation'''
    print(f'A {shape} with side {side:.2f} has area {area:.3f}')
# example function call:
# printresult(<string of shape name>, <float of side>, <float of area>)
# here I will input the side lengths
sideLength = float(input("Please enter the side length: "))
printresult('triangle', sideLength, (sqrt(3)/4)*(sideLength**2))
printresult('square', sideLength, sideLength**2)
printresult('pentagon', sideLength, (1/4)*sqrt(5*(5+2*sqrt(5)))*(sideLength**2))
printresult('dodecagon', sideLength, 3*(2+sqrt(3))*(sideLength**2))
#


