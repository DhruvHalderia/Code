# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         DHRUV HALDERIA
# Section:      503
# Assignment:   LAB 11.13
# Date:         11/14/22
#
#This opens the csv file
myFile = open('WeatherDataCLL.csv', 'r')
dataOfTemp = {}
num = 0
#this puts all the data into a dictionary
for line in myFile.readlines():
    if num !=0:
        tempList = line.strip().split(',')
        dataOfTemp[tempList[0]] = tempList[1:]
    num+=1
#the code below will get the max and min temps for the data
maxTemp = int(dataOfTemp['1/1/2019'][-2])
minTemp = int(dataOfTemp['1/1/2019'][-1])
avgPrecip = 0
num = 0 
for i in dataOfTemp:
    if int(dataOfTemp[i][-2]) > maxTemp:
        maxTemp = int(dataOfTemp[i][-2])
    if int(dataOfTemp[i][-1]) < minTemp:
        minTemp = int(dataOfTemp[i][-1])
    avgPrecip+= float(dataOfTemp[i][1])
    num+=1
avgPrecip/=num
print(f'3-year maximum temperature: {maxTemp} F')
print(f'3-year minimum temperature: {minTemp} F')
print(f'3-year average precipitation: {avgPrecip:.3f} inches\n')
#i created a month dictionary to assign months to a numeric value
monthDictionary = {'January': 1, 'February': 2, 'March': 3, 'April': 4,'May': 5,'June': 6,'July': 7,'August': 8,'September': 9,'October': 10,'November': 11,'December': 12, }

userMonth =input('Please enter a month: ')
userYear = input('Please enter a year: ')
print(f'\nFor {userMonth} {userYear}:')
userMonth = monthDictionary[userMonth]
meanTemp = 0
meanSpeed = 0
precipDays = 0
num = 0
# i assigned all the temps, speeds and precipitation in the for loop below
for i in dataOfTemp:
    tempList = i.split('/')
    if int(tempList[0]) == userMonth and tempList[-1] == userYear:
        num+=1
        meanSpeed+= float(dataOfTemp[i][0])
        meanTemp+= float(dataOfTemp[i][-2])
        if float(dataOfTemp[i][1])>0:
            precipDays+=1
meanTemp/=num
meanSpeed/=num
precipDays/=num
precipDays*=100
#I printed my data down below
print(f'Mean maximum daily temperature: {meanTemp:.1f} F')
print(f'Mean daily wind speed: {meanSpeed:.2f} mph')
print(f'Percentage of days with precipitation: {float(precipDays):.1f}%')


        
