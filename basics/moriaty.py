n = int(input())
ls = list(map(int,input().strip().split(' ')))
c = 0
k = 0
for i in range(len(ls)-2):
    if ls[i] == ls[i + 1]:
        if ls[i + 1] != ls[i+2]:

            k = 2
            c= c+ k
            k = 0
        elif ls[i + 1] == ls[i+2]:

            k  =  3
            c=c+k
            k = 0

print(c)