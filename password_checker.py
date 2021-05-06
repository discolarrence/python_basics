import sys

password = input("Please enter the password:  ")
attempt_count = 1
while password != "opensesame":
    if attempt_count > 3:
        sys.exit("Too many invalid password attempts")
    password = input("Invalid password, try again: ")
    attempt_count += 1
print("Welcome to secret town")