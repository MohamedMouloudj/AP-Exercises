runner1_name = input("Enter the name of Runner 1: ")
runner1_time = float(input("Enter the time (in seconds): "))

runner2_name = input("Enter the name of Runner 2: ")
runner2_time = float(input("Enter the time (in seconds): "))

if runner1_time < runner2_time:
    print(runner1_name, "is the faster runner")
elif runner1_time > runner2_time:
    print(runner2_name, "is the faster runner")
else:
    print("Both runners have the same time!")