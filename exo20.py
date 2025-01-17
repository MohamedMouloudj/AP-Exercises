numbers=[]

number=int(input("Enter a number: "))
while number != 0:
    numbers.append(number)
    number=int(input("Enter a number: "))
print("Current list: ", str(numbers))
print("Sorted list: ", str(sorted(numbers)))
