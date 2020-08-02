

ls = [1,2,3,4,5]

k = 4
print(ls)
temp = 0
for k in range(k):

    for i in range(k):
        for j in range(len(ls)-1,0,-1):
            temp = ls[j]
            ls[j] = ls[j-1]
            ls[j-1] = temp


print(ls)