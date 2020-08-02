n = int(input())
vowels = 'aeiou'
c = 0
for i in range(n):
    str = input()
    for k in range(len(str)):
        if str[k] in vowels:
            c +=1

    print(c)
    c = 0