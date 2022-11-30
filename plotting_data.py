# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         DHRUV HALDERIA
# Section:      503
# Assignment:   LAB 12.17
# Date:         11/28/22
#
import matplotlib.pyplot as plt
import numpy as np
#below is the code from my previous submission that i am using as allowed in the instructions 
myFile = open('WeatherDataCLL.csv', 'r')
dataOfTemp = {}
num = 0
#this puts all the data into a dictionary
for line in myFile.readlines():
    if num !=0:
        tempList = line.strip().split(',')
        dataOfTemp[tempList[0]] = tempList[1:]
    num+=1
maxTemp = []
avgWindSpeed = []
minTemp = []
amountOfDays = np.arange(len(dataOfTemp))
for i in dataOfTemp:
    maxTemp+=[int(dataOfTemp[i][-2])]
    avgWindSpeed +=[float(dataOfTemp[i][0])]
    minTemp+=[float(dataOfTemp[i][-1])]
#below the first figure is being made into a graph
plt.figure(1)
lns = plt.plot(amountOfDays, maxTemp,'r', label = 'Max Temp')
plt.xlabel("date")
plt.ylabel('Maximum Temperature, F')
#above i made my first y-axis graph and below they are going to share the same x axis 
plt.twinx()
ln2 = plt.plot(amountOfDays, avgWindSpeed,'b', label = 'Avg Wind')
plt.ylabel('Average Wind Speed, mph')
ln3 = lns + ln2
labs = [i.get_label() for i in ln3]
#above the labels are combined into a list to put it onto the same legend
plt.legend(ln3, labs, loc = "lower left")
plt.title("Maximum temperature and Average Wind Speed")
plt.tight_layout()


plt.figure(2)
plt.hist(avgWindSpeed, 27,  edgecolor = 'black', color='green')
plt.title('Histogram of average wind speed')
plt.xlabel('Average Wind Speed, mph')
plt.ylabel('Number of days')



plt.figure(3)
plt.scatter(minTemp,avgWindSpeed, c= 'black',marker = '.')
plt.xlabel('Minimum Temperature, F')
plt.ylabel('Average Wind Speed, mph')
plt.title('Average Wind Speed vs Minimum Temperature')



tempsAvg = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:[], 12:[]}
tempsMax = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:[], 12:[]}
tempsMin = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:[], 12:[]}


for i in dataOfTemp:
    tempList = i.split('/')
    if (tempList[0] == '1'):
        tempsAvg[1] +=[int(dataOfTemp[i][2])]
        tempsMax[1] +=[int(dataOfTemp[i][-2])]
        tempsMin[1] +=[int(dataOfTemp[i][-1])]
    elif tempList[0] == '2':
        tempsAvg[2] +=[int(dataOfTemp[i][2])]
        tempsMax[2] +=[int(dataOfTemp[i][-2])]
        tempsMin[2] +=[int(dataOfTemp[i][-1])]
    elif tempList[0] == '3':
        tempsAvg[3] +=[int(dataOfTemp[i][2])]
        tempsMax[3] +=[int(dataOfTemp[i][-2])]
        tempsMin[3] +=[int(dataOfTemp[i][-1])]
    elif tempList[0] == '4':
        tempsAvg[4] +=[int(dataOfTemp[i][2])]
        tempsMax[4] +=[int(dataOfTemp[i][-2])]
        tempsMin[4] +=[int(dataOfTemp[i][-1])]
    elif tempList[0] == '5':
        tempsAvg[5] +=[int(dataOfTemp[i][2])]
        tempsMax[5] +=[int(dataOfTemp[i][-2])]
        tempsMin[5] +=[int(dataOfTemp[i][-1])]
    elif tempList[0] == '6':
        tempsAvg[6] +=[int(dataOfTemp[i][2])]
        tempsMax[6] +=[int(dataOfTemp[i][-2])]
        tempsMin[6] +=[int(dataOfTemp[i][-1])]
    elif tempList[0] == '7':
        tempsAvg[7] +=[int(dataOfTemp[i][2])]
        tempsMax[7] +=[int(dataOfTemp[i][-2])]
        tempsMin[7] +=[int(dataOfTemp[i][-1])]
    elif tempList[0] == '8':
        tempsAvg[8] +=[int(dataOfTemp[i][2])]
        tempsMax[8] +=[int(dataOfTemp[i][-2])]
        tempsMin[8] +=[int(dataOfTemp[i][-1])]
    elif tempList[0] == '9':
        tempsAvg[9] +=[int(dataOfTemp[i][2])]
        tempsMax[9] +=[int(dataOfTemp[i][-2])]
        tempsMin[9] +=[int(dataOfTemp[i][-1])]
    elif tempList[0] == '10':
        tempsAvg[10] +=[int(dataOfTemp[i][2])]
        tempsMax[10] +=[int(dataOfTemp[i][-2])]
        tempsMin[10] +=[int(dataOfTemp[i][-1])]
    elif tempList[0] == '11':
        tempsAvg[11] +=[int(dataOfTemp[i][2])]
        tempsMax[11] +=[int(dataOfTemp[i][-2])]
        tempsMin[11] +=[int(dataOfTemp[i][-1])]
    elif tempList[0] == '12':
        tempsAvg[12] +=[int(dataOfTemp[i][2])]
        tempsMax[12] +=[int(dataOfTemp[i][-2])]
        tempsMin[12] +=[int(dataOfTemp[i][-1])]
        

maxTemperature = []
minTemperature = []
averageTemperature = []
xAxis = []
for i in range(12):
    xAxis+=[i+1]
for i in tempsMax:
    maxTemperature +=[max(tempsMax[i])]
for i in tempsMin:
    minTemperature +=[min(tempsMin[i])]
for i in tempsAvg:
    averageTemperature += [sum(tempsAvg[i])/len(tempsAvg[i])]
plt.figure(4)
plt.bar(xAxis, averageTemperature, color= '#bfbf00')
plt.plot(xAxis, minTemperature,'b', label = 'Low T')
plt.plot(xAxis,maxTemperature,'r', label = 'High T')
plt.legend()
plt.title("Temperature by month")
plt.ylabel("Average Temperature, F")
plt.xlabel("Month")

plt.show()
