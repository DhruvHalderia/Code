# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:   Dhruv Halderia
# Section:      503
# Assignment:   5.4
# Date:         09/26/2022

import math

def getHeatFlux(y0, x, x0, x1, y1):
    # this calculates the heat flux for the point entered by the user
    mVal = math.log10(y1/y0)/math.log10(x1/x0)
    tempVal = y0 * ((x/x0)**mVal)
    print(f"The surface heat flux is approximately {round(tempVal)} W/m^2") #This if for zybooks point

#This if for zybooks point
mainPoint = float(input("Enter the excess temperature: "))
#this tells the user if the input is in the bounds of the points
if(mainPoint < 1.3 or mainPoint> 1200):
    print("Surface heat flux is not available")

else:
#These initial if statements get the heat flux if the user inputs a given point in the program
    if(mainPoint == 1.3):
        print("The surface heat flux is approximately 1000 W/m^2")
    if(mainPoint == 5):
        print("The surface heat flux is approximately 7000 W/m^2")
    if(mainPoint == 30):
        print("The surface heat flux is approximately 1500000 W/m^2")
    if(mainPoint == 120):
        print("The surface heat flux is approximately 25000 W/m^2")#This if for zybooks point
    if(mainPoint == 1200):
        print("The surface heat flux is approximately 1500000 W/m^2")
#These get the heatflux for the bounds that the user enters in
    if(mainPoint >1.3 and mainPoint < 5):
        getHeatFlux(1000, mainPoint, 1.3, 5, 7000)
    if(mainPoint >5 and mainPoint <30):
        getHeatFlux(7000, mainPoint, 5, 30, 1500000)
    if(mainPoint > 30 and mainPoint <120):
        getHeatFlux(1500000, mainPoint, 30, 120, 25000) #This if for zybooks point
    if(mainPoint > 120 and mainPoint < 1200):
        getHeatFlux(25000, mainPoint, 120, 1200, 1500000)
#This if for zybooks point