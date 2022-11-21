
myFile = open('mod12activity.txt', 'r')
myArr1 = []
myArr2 = []
myArr3 = []
myArr4 = []
myArr5 = []
num = 0
iterator = 0
for i in myFile.readlines():
    if iterator == 5:
        iterator = 0
        num+=1
    if iterator < 5 and num == 0: 
        myArr1+=i.strip()
        iterator+=1
    elif iterator < 5 and num == 1: 
        myArr2+=i.strip()
        iterator+=1
    elif iterator < 5 and num == 2: 
        myArr3+=i.strip()
        iterator+=1
    elif iterator < 5 and num == 3: 
        myArr4+=i.strip()
        iterator+=1
    elif iterator < 5 and num == 4: 
        myArr5+=i.strip()
        iterator+=1
print(myArr1)
print(myArr2)
print(myArr3)
print(myArr4)
print(myArr5)
    
    
     
    