valid_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

total_amount=int(input("Total amount: "))
number_items=int(input("Number of items: "))
day_of_week=input("Day of the week: ")

if day_of_week in valid_days:
    if day_of_week in valid_days[0:5]:
        discount=0.1
    else:   
        discount=0.2
    if number_items>5:
        discount+=0.05
    total_amount=total_amount*(1-discount)
    print(f"Total amount after discount: {total_amount} dinars")
else:
    print("Invalid day of the week")