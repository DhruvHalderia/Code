# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Tilman Strickland
#               Dhruv Halderia
#               Logan Stringer
# Section:      503
# Assignment:   4.13
# Date:         09/18/2022
############ Part A ############
a = input("Enter True or False for a: ")
b = input("Enter True or False for b: ")
c = input("Enter True or False for c: ")

#setting a boolean
if(a == "True" or a == "t" or a =="T" ):
    aBool = True
else:
    aBool = False

#setting b boolean
if(b == "True" or b == "t" or b =="T" ):
    bBool = True
else:
    bBool = False

#setting c boolean
if(c == "True" or c == "t" or c =="T" ):
    cBool = True
else:
    cBool = False

############ Part B ############
print(f"a and b and c: {aBool and bBool and cBool == True}")
print(f"a or b or c: {aBool or bBool or cBool == True}")

############ Part C ############

print(f"XOR: {(aBool and bBool == False) or (aBool == False and bBool)}")
print(f"Odd number: {((aBool and bBool == False and cBool == False)) or ((cBool and bBool == False and aBool == False)) or ((bBool and aBool == False and cBool == False)) or ((aBool and bBool and cBool)) }")

############ Part D ############

#complex1
comp1 = (not (aBool and not bBool) or (not cBool and bBool) )and (not bBool) or (not aBool and bBool and not cBool) or (aBool and not bBool)
print(f"Complex 1: {comp1}")

#complex2
comp2 = (not ((bBool or not cBool) and (not aBool or not cBool))) or (not (cBool or not (bBool and cBool))) or (aBool and not cBool) and (not aBool or (aBool and bBool
and cBool) or (aBool and ((bBool and not cBool) or (not bBool))))
print(f"Complex 2: {comp2}")


#simple1
simp1 = ((bBool or (aBool and not bBool)))
print(f"Simple 1: {simp1}")

#simple2
simp2 = ((not bBool and cBool) or (aBool))
print(f"Simple 2: {simp2}")
