# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Tilman Strickland
#               Dhruv Halderia
#               Logan Stringer
# Section:      503
# Assignment:   4.13
# Date:         09/16/2022
# i am gathering the coefficient  values here
ACof = int(float(input("Please enter the coefficient A: ")))
BCof = int(float(input("Please enter the coefficient B: ")))
CCof = int(float(input("Please enter the coefficient C: ")))
# this is the equation the answer will be in
equation = ""
#calculate a coefficient
if(ACof != 0):
    if(ACof == 1 or ACof == -1):
        if(ACof == -1):
            equation = equation + "- x^2 "
        else:
            equation = equation + "x^2 "
    elif(ACof < 0):
        equation = equation + "- " + str(ACof*-1) + "x^2 "
    else:
        equation = equation + str(ACof) + "x^2 "
#calculate b coefficient
if(BCof != 0):
    if(BCof == 1 or BCof == -1):
        if(BCof == -1):
            equation = equation + "- x "
        else:
            if(ACof !=0):
                equation = equation +"+ x "
            else:
                equation = equation+"x "
    elif(BCof < 0):
        equation = equation + "- " + str(BCof*-1) + "x "
    else:
        if(ACof !=0):
            equation = equation +"+ "+ str(BCof) + "x "
        else:
            equation = equation+str(BCof)+"x "
#calculate c coefficient
if(CCof != 0):
    if(CCof == 1 or CCof == -1):
        if(CCof == -1):
            equation = equation+"- 1 "
        else:
            equation = equation +"+ 1 "
    elif(CCof < 0):
        equation = equation + "- " + str(CCof*-1)+" "
    else:
        equation = equation +"+ "+ str(CCof)+" "
print("The quadratic equation is",equation+"= 0")
