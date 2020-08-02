ar = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
m = set(ar)
s = input().strip()
s = s.lower()
j = ""
for i in range(len(s)):
    if s[i]== " ":
        j = j
    else:
        j = j + s[i]
k = set(j)
print(m)
print(k)
if m == k:
    print('pangram')
else:
    print('not pangram')