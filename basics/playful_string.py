n = int(input())

for k in range(n):

    word = input()
    for i in range(len(word)):
        for character in word:

             if ord(character)+1 == ord(word[i+1]):
                 print('YES')

             elif ord(character) == 97:
                 if word[i+1] == 122:
                     print('YES')
             else:
                 print('NO')