age_first_person = int(input("Age of the first person: "))
age_second_person = int(input("Age of the second person: "))
if age_first_person != age_second_person:
    print("The older age is: ", max(age_first_person, age_second_person))
else:
    print("Both people are the same age!")