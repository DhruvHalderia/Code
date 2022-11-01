# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         DHRUV HALDERIA
# Section:      503
# Assignment:   LAB 10.14
# Date:         31 OCTOBER 2022
#
#below i have made a check input function that takes in an input and checks if it is valid or not 
def checkInput():
    go = False
    num = 0
    while not go:
#I used a try statement down below to test if the code will give me an error and it will repeat since it is in a while loop 
        try: 
            if(num ==0 ):
                userNum = int(input("What is your guess? "))
                go = True
            else:
                userNum = int(input("Try again: "))
                go = True
#this is an except statement which will throw a message when ever an exception occurs and will force to try again 
        except:
            num +=1
            print("Bad input!", end=" ")
#this will return a number which is the users guess into the main method 
    return userNum     

#this will check the location of the guess number in comparison to the secret number and return an appropriate statement 
def checkLocation(num,secNum,num2):
    if num > secNum:
        return "Too high!"
    if num < secNum: 
        return "Too low!"
    else:
        return "You guessed it! It took you "+str(num2)+" guesses."

#this is the main method that will call all the functions and will have the function running until the user guesses the number
if __name__ == '__main__':
    secretNum = 26
    go = False
    guessNum = 0
    checkCount = 0
    print("Guess the secret number! Hint: it's an integer between 1 and 100... ")
#this while loop will keep it running until the user gets the number right
    while guessNum != secretNum:
        guessNum = checkInput()
        checkCount+=1
        print(checkLocation(guessNum, secretNum, checkCount))

    
    