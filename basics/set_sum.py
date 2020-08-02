ls = [1,2,3,4,5,1,5,2]
s =set(ls)
k = len(s)
print(len(s))
sum = 0
for i in range(len(s)):
    sum = sum + s.pop()

print(sum/k)