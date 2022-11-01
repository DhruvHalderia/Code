# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Tilman Strickland
#               Dhruv Halderia
#               Logan Stringer
# Section:      503
# Assignment:   9.15
# Date:         10/31/2022
#this gets the data points for the polygon
def getpoints(a):
    anslist = []
    mylist = a.split(' ')
    for i in mylist:
        b = i.split(',')
        anslist.append([int(b[0]),int(b[1])])
    return anslist

#this does the cross multiplication to solve for the answer
def cross(a,b):
    prod = ((a[0])*(b[1])-((a[1])*(b[0])))
    return prod

#this gets the area of the polygon
def shoelace(anslist):
    c= cross(anslist[-1], anslist[0])
    for i in range(len(anslist)-1):
        c += cross(anslist[i],anslist[i+1])
    area = c/2
    return area

#this calls the functions
def main():
    print("The area of the polygon is",shoelace(getpoints(input("Please enter the vertices: "))))
    
#this calls the main function    
if __name__ == '__main__': 
    main() 
