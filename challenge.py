name = input("Please enter your name: ")
number = int(input("Please enter a number: "))
print(name, "\n", number)
is_fizz = bool(number % 3 == 0)
is_buzz = bool(number % 5 == 0)
if is_fizz and is_buzz:
    print(number, "is a FizzBuzz number")
elif is_fizz:
    print(number, "is a Fizz number")
elif is_buzz:
    print(number, "is a Buzz number")
else: 
    print(number, "is neither a fizzy nor a buzzy number")