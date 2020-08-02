m = int(input())
ls = []
for i in range(m):
    lso = int(input().strip())
    ls.append(lso)

ls1 = []

for k in range(len(ls)):
    if ls[k] >= 40:
        if (ls[k] + 2) % 5 == 0 or (ls[k]+1)% 5 == 0:
            if (ls[k] + 2) % 5 == 0:
                ls1.append(ls[k]+2)

            elif (ls[k] + 1 % 5) == 0:
                ls1.append(ls[k]+1)

        else:
            ls1.append(ls[k])

    elif ls[k] < 40 and ls[k] != 0:
        if (ls[k] + 2) % 5 == 0:
            if (ls[k]+2) == 40:
                ls1.append(ls[k]+2)
            else:
                ls1.append(ls[k])
        else:
            ls1.append(ls[k])

for w in range(len(ls1)):
    print(ls1[w],end="\n")