# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         DHRUV HALDERIA
# Section:      503
# Assignment:   LAB 12.17
# Date:         11/26/22
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

#below the average wind speed data is being collected

#below is my figure 2
plt.figure(2)


plt.figure(3)
plt.scatter(minTemp,avgWindSpeed, c= 'black',marker = '.')
plt.xlabel('Minimum Temperature, F')
plt.ylabel('Average Wind Speed, mph')
plt.title('Average Wind Speed vs Minimum Temperature')
plt.show()