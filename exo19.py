import os

unique_words = set()
if os.path.exists("unique_words.txt"):
    with open("unique_words.txt","r") as file:
        for line in file:
            unique_words.add(line.strip())

exist=False
while not exist:
    word = input("Enter a word: ")
    if word in unique_words:
        exist=True
    else:
        unique_words.add(word)

print("You entered an already existing word")
response=input("Would you like to save the words in a file? Press Enter to continue...")

if response == "":
    with open("unique_words.txt","r") as file:
        lines = file.read().split("\n")
    with open("unique_words.txt","a") as file:
        for word in unique_words:
            if word not in lines:
                file.write(word+"\n")
            
    print("Words saved in words.txt")