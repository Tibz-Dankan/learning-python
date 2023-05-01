# if statement
if 15> 10:
    print("15 is greater than 10")
print("Program Ended")

# Nested if statement
num = 20
if num > 10:
    print("num is greater than 10")
    if num <= 31:
        print("num lies btn 10 and 31")
    
# Note: if statements depend on indentation

# If else statement
num = 3
if num == 1:
    print("One")
else:
    if num == 2:
      print("Two")
    else:
        if num == 3:
            print("Three")
        else:
            print("Something else")

# elif statement( short hand for else if)
num = 3
if num == 1:
    print("One")
elif num == 2:
    print("Two")
elif num == 3:
    print("Three")
else:
    print("Something else")