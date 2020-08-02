s = "abc"
words = 0
i = 0

if s.islower():
    words = 1
else:

    if s[i].islower():
        words = words + 1
    i = i + 1

    while s[i].islower():
        i = i + 1
    if i < len(s):
        for i in range(len(s)):
            if s[i].isupper():
                words += 1

print(words)
