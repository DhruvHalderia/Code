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

#establishing inputs
pay = float(input("How much did you pay? "))
cost = float(input("How much did it cost? "))
diff = pay - cost
print(f"You received ${diff:.2f} in change. That is...")
diff*=100
diff = round(diff)
#calculating the amount of coins returned
if(diff>=0):
# calculating quarters
    if(diff>=25):
        quarters = diff // 25
        if(quarters == 1):
            print(int(quarters), "quarter")
        else:
            print(int(quarters),"quarters")
        diff = diff%25

#calculating dimes
    if(diff>=10):
        dime = diff // 10
        if(dime == 1):
            print(int(dime), "dime")
        else:
            print(int(dime),"dimes")
        diff = diff%10
# calculating nickels
    if(diff>=5):
        nickel = diff // 5
        if(nickel == 1):
            print(int(nickel), "nickel")
        else:
            print(int(nickel),"nickels")
        diff = diff%.05
#calculating pennies
    if(diff >=1):
        pennies = diff//1
        if(pennies == 1):
            print(int(pennies), "penny")
        else:
            print(int(pennies),"pennies")
        diff = diff%1
else:
    print("ERROR there is insufficient funds to complete this transaction")
#