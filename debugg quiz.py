# the below code will get inputs from the user:

number = int(float(input("Enter a 5-digit integer: ")))

# the code below will get the individual numbers

originalNum = number

num1 = number // 10000

number = number% 10000

num2 = number//1000

number = number% 1000

num3 = number//100

number = number% 100

num4 = number//10

number = number% 10

num5 = number

print(f"{originalNum} backwards is: {num5}{num4}{num3}{num2}{num1}")