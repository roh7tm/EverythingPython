n = 12
word = 'Hello_World!'
k = 4
p = 0

result = ""
for i in range(n):
    j = ord(word[i])
    if j == 90:
        p = 64
        m = chr(p + k)

    elif j == 122:
        p = 96
        m = chr(p + k)

        result = result + m


    elif j >= 65 and j<=90 or j >= 97 and j <= 122:
        m = chr(j + k)

        result = result + m

    else:

        result = result + word[i]


print(result)