ls = list(map(int,input().strip().split(' ')))
s =set(ls)
ls = list(s)
ls.sort()



k = ls[0]
l = ls[len(ls)-1]
st = set()

for i in range(k, l + 1):
     st.add(i)

if s==st:
    print('YES')

else:
    print('NO')
