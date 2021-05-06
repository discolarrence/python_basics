TICKET_PRICE = 10

SERVICE_CHARGE = 2

tickets_remaining = 100  

def calculate_price(tickets_wanted):
    return (tickets_wanted * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining >= 1:
    print("There are {} tickets remaining".format(tickets_remaining))
    user_name = input("What is your name?  ")
    try:
        tickets_wanted = int(input("Hi, {}. How many tickets do you want?  ".format(user_name)))
        if tickets_wanted > 100:
            raise ValueError("You requested more tickets than available.")
    except ValueError as err:
        print("Oh no! That's not a valid value. Try again....")
        print("({})".format(err))
    else:
        total_price = calculate_price(tickets_wanted)
        print("The total price for {} tickets is ${}.".format(tickets_wanted, total_price))
        confirm = input("Would you like to proceed? y/n  ")
        if confirm.lower() == "y":
            #TODO: Gather cc info and process
            print("SOLD! {} tickets for you!".format(tickets_wanted))
            tickets_remaining -= tickets_wanted
        else:
            print("Thank you, {}. Come back and see us if you change your mind.".format(user_name))  
print("Tickets are now sold out for this show!")
