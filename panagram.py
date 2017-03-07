from string import ascii_lowercase
sentence = str(input(" please enter your word: ")).strip().lower()
list2 = [letter for letter in sentence if letter.isalpha()]
alphabet = "abcdefghijklmnopqrstuvwxyz"

for char in alphabet:
    if char not in list2:
        False
print('It is a panagram')

if set(sentence).issuperset(set(ascii_lowercase)):
    print('panagram')
else:
    print('no panagram')
