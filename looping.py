name = input("What's your name? ")
user_understands = input("Do you understand while loops, {}? yes/no ".format(name))

while user_understands == "no":
    print("The while loop in Python is used to iterate over a block of code as long as the test expression (condition) is true. We generally use this loop when we don't know the number of times to iterate beforehand.")
    user_understands = input("Do you understand while loops, {}? yes/no ".format(name))
    
print("Congratulations for understanding while loops!")