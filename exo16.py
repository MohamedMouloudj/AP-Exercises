numbers = [1, 2, 3, 4, 5]

print("Inex = -1 to quit")
index=int(input("Enter index: "))
while index != -1:
    if index >= len(numbers):
        print("Index out of range")
    else:
        value=int(input("Enter value: "))
        numbers[index]=value
        print(numbers)
    index=int(input("Enter index: "))