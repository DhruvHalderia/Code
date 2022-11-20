# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Tilman Strickland
#               Dhruv Halderia
#               Logan Stringer
# Section:      503
# Assignment:   11.9
# Date:         11/19/2022 
def checker(a):
    mydiction = {}
    for i in a:
        if i !='':
            mydiction[i[:3]]= i[4:]
    try:
        if(len(mydiction) >= 7 and mydiction['ecl'] != 'None' and mydiction['pid'] != 'None' and mydiction['byr'] != 'None' and mydiction['hgt'] != 'None' and mydiction['iyr'] != 'None' and mydiction['eyr'] != 'None' and mydiction['cid'] != 'None'):
            if(int(mydiction['byr']) >= 1920 and int(mydiction['byr']) <= 2005) and (int(mydiction['iyr']) >= 2012 and int(mydiction['iyr']) <= 2022) and (mydiction['ecl'] == 'amb' or mydiction['ecl'] == 'blu' or mydiction['ecl'] == 'brn' or mydiction['ecl'] == 'gry' or mydiction['ecl'] == 'grn' or mydiction['ecl'] == 'hzl' or mydiction['ecl'] == 'oth') and (int(mydiction['eyr']) >=2022 and int(mydiction['eyr']) <=2032 ):
                metric = mydiction['hgt'][-2:]
                num = int(mydiction['hgt'][:-2])
                if (metric == 'in' and num >= 59 and num <= 76):
                    if(len(mydiction['pid']) == 9):
                        newCid = mydiction['cid'].lstrip('0')
                        if(len(newCid) == 3):
                            return mydiction
                elif(metric == 'cm' and num>= 150 and num<= 193):
                    if(len(mydiction['pid']) == 9):
                        newCid = mydiction['cid'].lstrip('0')
                        if(len(newCid) == 3):
                            return mydiction
    except:
        return {}
    return {}
        
#get the file name here
user = input('Enter the name of the file: ')
myfile = open(user, 'r')
endFile = open('valid_passports2.txt', 'w')
mylist = []
mystr = ''
totalPass = 0
endLine = ''
#read each file line and put it into a list to call the function checker
for line in myfile.readlines():
    endLine += line
    if line.strip() == '':
        templist = mystr.split(' ')
        tempDictionary = checker(templist[0:-1])
        if(len(tempDictionary) >0):
#check in the for loop up above
            totalPass +=1
            endFile.write(endLine)
        mystr = ''
        endLine = ''
    mystr += line.strip() + ' '
templist = mystr.split(' ')
tempDictionary = checker(templist[0:-1])
if(len(tempDictionary) >0):
#check the last element here
    totalPass +=1
    endFile.write(endLine)
print(f'There are {totalPass} valid passports')
endFile.close()
myfile.close()

