
arr = list(map(int, input().strip().split(' ')))

arr.sort()
max_sum = 0
min_sum = 0

for i in range(len(arr)-1,0,-1):
    max_sum = max_sum + arr[i]

for i in range(len(arr)-1):
    min_sum = min_sum + arr[i]

print(max_sum)
print(min_sum)