n = int(input())

k =list(map(int, input().strip().split(' ')))
sum = 1
i =0
while n > 0:
    sum =  sum * k[i]
    i = i + 1
    n = n-1

print(sum)