ls = [1 ,2, 3, 4, 5]
range2=1
c = 0
j = 0
la = [0,0,0,0,0]
for i in range(len(ls)-1):
    if la[i] == 0:
        while range2 < 1:
            j = i + 1
            range2 -=1

        la[j] = 1
        la[j-1]=1
        la[j+1]=1

    i = j+2



print(la)

