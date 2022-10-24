# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         DHRUV HALDERIA
# Section:      503
# Assignment:   LAB 9.16
# Date:         24 October 2022
#
#
import math

def parta(radiusS, radiusH):
    if radiusH > radiusS:
        return 0
    v = (4*math.pi/3)*((radiusS**2)-(radiusH**2))**(3/2)
    return v
 
#making partb below
def partb(n):
    #making a num list to store all the numbers in 
    numList = []
    # the for loop will go through the all the odd numbers in the list and determine if they will add up to n
    total = 0
    for i in range(n):
        total = 0 
        numList = []
        for j in range(i,n):
            if j%2 !=0:
                total+=j
                numList.append(j)
            if total == n:
                return numList
            if total > n:
                total = 0 
                numList = []
    return False

# i made partc on the bottom
def partc(border, name, place, mail):
    card =""
    if (len(name)> len(place)) and (len(name)> len(mail)):
        longString = name
    elif(len(name)< len(place)) and (len(place)> len(mail)):
        longString = place
    else:
        longString = mail
    card+=border+"".center(len(longString)+5,border)+"\n"
    card+= border+name.center(len(longString)+4)+border+"\n"
    card+=border+place.center(len(longString)+4)+border+'\n'
    card+=border+mail.center(len(longString)+4)+border+'\n'
    card+=border+"".center(len(longString)+5,border)
    return card

#below i am making part d
def partd(numList):
    ansList = []
    numList.sort()
    ansList.append(numList[0])
    if len(numList)%2 == 0:
        ansList.append((numList[len(numList)//2] + numList[len(numList)//2 -1])/2)
    else:
        ansList.append(numList[len(numList)//2])
    ansList.append(numList[-1])
    return tuple(ansList)

#below i am making part e
def parte(times, distance):
    velocity_list = []
    for i in range(len(times)-1):
        velocity_list.append(((distance[i]-distance[i+1])/(times[i]-times[i+1])))
    return velocity_list

#below i am making part f for the code
def partf(a):
    ans = 0
    for i in range(len(a)):
        for j in range(i):
            if a[i] + a[j] == 2026:
                ans = a[i] * a[j]
    return ans

'''
#testing the parts with test cases
print(parta(9,2))
print(partb(3))
print(partc('*', 'Dr. Ritchey', 'Texas A&M University','snritchey@tamu.edu'))
a = [1,2,4,5,7,6,9]
print(partd(a))
b = [3,4,5,6,7,8,9]
print(parte(a,b))
numList = [1204, 3, 4, 5, 6, 822]
print(partf(numList))
'''
