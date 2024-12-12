vowels = ['a','e','o'] # Defined by the exercise

string=input("Please type in a string: ").lower()
is_a_found=string.find('a')!=-1
is_e_found=string.find('e')!=-1
is_o_found=string.find('o')!=-1

if is_a_found:
    print("a found")
else:
    print("a not found")

if is_e_found:
    print("e found")
else:
    print("e not found")

if is_o_found:
    print("o found")
else:
    print("o not found")