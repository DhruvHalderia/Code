#below i am making a dictionary that includes the letters to digit values 
letterToDigits = {'A':2, 'B' :2, 'C': 2, 'D':3, 'E' :3,'F': 3, 'G' : 4, 'H' : 4, 'I': 4, 'J': 5, 'K': 5, 'L': 5, 'M': 6,'N': 6, 'O': 6, 'P': 7, 'Q': 7, 'R': 7, 'S': 7, 'T' : 8,'U' : 8,'V': 8, 'W' : 9, 'X' : 9, 'Y' : 9, 'Z': 9}
#below i get the phone number from the user and then put it into a list 
phoneNumber = input("Enter a phone number in this format XXX-XXXXXXX: ")
numList = phoneNumber.split("-")
print(f"{phoneNumber} is equivalent to {numList[0]}", end="-")
#below i converted the line to a seperate word and then use the dictionary to make it the right number
word = numList[1]
for i in range(len(word)):
	if i !=3:
		print(letterToDigits[word[i]],end="")
	else:
		print(f"-{letterToDigits[word[i]]}", end="")
	