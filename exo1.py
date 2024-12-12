TICKET_COST=15.50
user_name=input("What is your name? ")
if user_name != "VIP":
    nb_tickets = int(input("How many tickets do you want to buy? "))
    total_cost = nb_tickets*TICKET_COST
    print("Total cost: ",total_cost)
    print("Enjoy the show!")
else:
    print("Enjoy the show for free!")
