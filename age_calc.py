name = input("What is your name?")
while True:
    try:
        year_born = int(input("What year were you born?"))
    except ValueError:
        continue
    else:
        break
        
ages = [25, 50, 75, 100]

from datetime import date
current_year = date.today().year

for age in ages:
    if year_born + age > current_year:
        print(name, "will turn", age, "in" , year_born + age)

