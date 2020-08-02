s = input()
new_string = ""
for character in s:

    if character.isupper():
        new_string = new_string + character.lower()
    elif character.islower():
        new_string = new_string + character.upper()

print(new_string)