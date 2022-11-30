number = input("Enter a number: ")  # assume the user enters 5.0 
try: 
    x = int(number) 
    print(f"x is the integer {x}") 
except: 
    x = float(number) 
    print(f"x is the float {x}") 