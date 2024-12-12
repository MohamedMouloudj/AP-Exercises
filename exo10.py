word=input("Please type in a word: ").split()[0].lower()
reverse_word=word[::-1]
if word==reverse_word:
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.")