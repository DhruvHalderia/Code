# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         DHRUV HALDERIA
# Section:      503
# Assignment:   LAB 7.25
# Date:         12 October 2022
#
#
# This collects the words from the user
words = input("Enter word(s) to convert to Pig Latin: ")
# this makes it into a list
words_list = words.split()
#below are the consonants and vowels
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
vowels = ["a", "e", "i", "o", "u", "y"]
print(f'In Pig Latin, "{words}" is:', end=" ")
#Below i have three if statements to find the pig latin parameters
for i in words_list:
     if i[0:1] in vowels: 
        print(i + "yay", end = " ")
     elif i[0:1] in consonants and i[1:2] in consonants: 
        print(i[2:] + i[0:2]+"ay", end= " ")
     elif i[0:1] in consonants:
        print(i[1:] + i[0:1]+"ay" , end = " " )
   