def anagrams(word1, word2):
    if len(word1) != len(word2):
        return False
    if word1 == word2:
        return True
    if word1 == "" or word2 == "":
        return False
    if not word1.isalnum() or not word2.isalnum():
        return False
    letters = sorted(word1)
    return letters == sorted(word2)

print(anagrams("listen", "silent")) # True
print(anagrams("hello", "world")) # False
print(anagrams("hello1", "hello1")) # True
print(anagrams("1234", "1234")) # True
