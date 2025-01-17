numbers = [1, 2, 3, 4, 5]

while True:
    print("1. Append")
    print("2. Insert element")
    print("3. Pop element")
    print("4. Remove element")
    print("5. Quit")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            numbers.append(int(input("Enter number to append: ")))
        case 2:
            index = int(input("Enter index to insert: "))
            value = int(input("Enter value to insert: "))
            numbers.insert(index, value)
        case 3:
            poped=numbers.pop()
            print("Poped element: "+str(poped))
        case 4:
            value = int(input("Enter value to remove: "))
            numbers.remove(value)
        case 5:
            break
        case _:
            print("Invalid choice")
    print("Updated list: "+str(numbers))
    