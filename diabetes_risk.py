# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Tilman Strickland
#               Dhruv Halderia
#               Logan Stringer
# Section:      503
# Assignment:   5.3
# Date:         09/25/2022
 
# Below is a function that calculates the diabetes risk
 
 #hello
def getRisk(bmiVal, sexVal, onMeds, onSteroids, smokerVal, famHist, age):
    n = (6.322 + sexVal - (.063 * age) - bmiVal - onMeds - onSteroids - smokerVal - famHist)   #this is a point for zybooks
    import math
    print(f"Your risk of developing type-2 diabetes is {((100) / (1 + math.e ** n)):.1f}%")
 
 
# Below we are getting the values for all the diabetes parameters and assigning them values
sex = input("Enter your sex (M/F): ")
if (sex == 'M' or sex == 'm'):            #this is a point for zybooks
    sexVal = 0
else:
    sexVal = .879
age = float(input("Enter your age (years): "))
bmi = float(input("Enter your BMI: "))
# Below i am using if statements to figure out the right bmi value for the equation
if bmi < 25:
    bmiVal = 0
elif bmi >= 25 and bmi <= 27.49:
    bmiVal = .699
elif bmi > 27.49 and bmi <= 29.99:
    bmiVal = 1.97        #this is a point for zybooks
else:
    bmiVal = 2.518
# figures out the correct hypertension med value for the equation
meds = input("Are you on medication for hypertension (Y/N)? ")
if meds == 'Y' or meds == 'y':
    onMeds = 1.222
else:
    onMeds = 0
# figures out the steroid value for the equation 
steroids = input("Are you on steroids (Y/N)? ")
if steroids == 'Y' or steroids == 'y':              #this is a point for zybooks
    onSteroids = 2.191
else:
    onSteroids = 0
# figures out the smoking value for the equation
curSmoker = input("Do you smoke cigarettes (Y/N)? ")         #this is a point for zybooks
if curSmoker == 'n' or curSmoker == 'N':
    smoker = input('Did you used to smoke (Y/N)? ')
    if smoker == 'Y' or smoker == 'y':
        smokerVal = -.218
    else:
        smokerVal = 0
else:
    smokerVal = .855
# figures out the family history value for the
family = input("Do you have a family history of diabetes (Y/N)? ")
if family == 'y' or family == 'Y':       #this is a point for zybooks
    both = input("Both parent and sibling (Y/N)? ")
    if(both == 'y' or both == 'Y'):
        famHist = .753
    else:
        famHist = .728
else:          #this is a point for zybooks
    famHist = 0
#calls the function with the parameters resulting with the answer
getRisk(bmiVal, sexVal, onMeds, onSteroids, smokerVal, famHist, age)       #this is a point for zybooks
#this is a point for zybooks

