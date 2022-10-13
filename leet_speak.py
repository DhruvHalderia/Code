# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         DHRUV HALDERIA
# Section:      503
# Assignment:   LAB 7.26
# Date:         12 October 2022
#
#gets the text into the program
text = input("Enter some text: ")
print(f'In leet speak, "{text}" is: ', end = " ")
#makes the list for the text entered
text_list = text.split()
text_dict = {"a": 4, "e": 3, "o": 0, "s": 5, "t": 7}
#assigns the numbers in the text
for i in text_list:
    for x in range(len(i)):
#checks if the letter is in the dictionary
        if i[x:x+1] in text_dict:
            print(text_dict[i[x:x+1]], end="")
        else:
            print(i[x:x+1], end="")
    print("", end=" ")
        
        
