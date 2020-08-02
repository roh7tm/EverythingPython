array_size , subs_k = input().strip().split(' ')
array_size , subs_k = [int(array_size) , int(subs_k)]
la = []

for i in range(array_size):
    la = la + [int(input().strip())]

print(la)
largest = 0
c = 1
ar = []
a = 1

for j in range(len(la)):
    a = la[j]
    for m in range(1,len(la)):
        a =a&la[m]

    ar = ar + [a]
print(ar)
print(ar.sort())
print(ar.reverse())
print(ar[0])

for i in range(len(ar)-1):
    while ar[i] == ar[i+1]:
        c +=1


print(c)












