people=int(input("How many people need a ride? "))
seats=int(input("How many people fit in one taxi? "))

taxis=people//seats
if people%seats>0:
    taxis+=1

print("Number of taxis needed: ",taxis)