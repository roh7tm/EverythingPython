st = input()
st = set(st)
c = 0
n = int(input())
for i in range(n):
    s1 = set(input())

    if s1 <= st:
        c = c+1

print(c)