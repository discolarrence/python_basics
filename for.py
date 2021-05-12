# Columns: Name, Day/Month, Celebrates, Age
BIRTHDAYS = (
    ("James", "9/8", True, 9),
    ("Shawna", "12/6", True, 22),
    ("Amaya", "28/2", False, 8),
    ("Kamal", "29/4", True, 19),
    ("Sam", "16/7", False, 22),
    ("Xan", "14/3", False, 34),
)

# Problem 1: Celebrations
# Loop through all of the people in BIRTHDAYS
# If they celebrate their birthday, print out
# "Happy Birthday" and their name

print("Celebrations:")
for person in BIRTHDAYS:
    if person[2] == True:
        print("Happy Birthday " + person[0])
# Solution 1 here

print("-"*20)

# Problem 2: Half birthdays
# Loop through all of the people in BIRTHDAYS
# Calculate their half birthday (six months later)
# Print out their name and half birthday
print("Half birthdays:")
for person in BIRTHDAYS:
    birthday = person[1]
    month = int(birthday[-1])
    if month < 7:
        half_month = str(month + 6)
    else:
        half_month = str(month - 6)
    half_birthday = birthday[:-1] + half_month
    print(person[0] + " " + half_birthday)
        
# Solution 2 here

print("-"*20)

# Problem 3: Only school year birthdays
# Loop through the people in BIRTHDAYS
# If their birthday is between September (9)
# And June (6), print their name
print("School birthdays:")
for person in BIRTHDAYS:
    month = int(person[1][-1])
    if month not in range(7, 9):
        print(person[0])
# Solution 3 here

print("-"*20)

# Problem 4: Wishing stars
# Loop through BIRTHDAYS
# If the person celebrates their birthday,
# AND their age is 10 or less,
# Print out their name and as many stars as their age
print("Stars:")
for person in BIRTHDAYS:
    if person[2] == True and person[3] <= 10:
        print(person[0] + "*"*person[3])
# Solution 4 here

print("-"*20)