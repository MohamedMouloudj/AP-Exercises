positive_int = int(input("Enter a positive integer: "))

while positive_int <= 0:
    print("The integer is not positive.")
    positive_int = int(input("Enter a positive integer: "))

for i in range(-positive_int, positive_int + 1, 1):
    if i != 0:
        print(i)