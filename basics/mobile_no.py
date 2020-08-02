n = int(input())
for i in range(n):
    s = input()
    if len(s) == 10 and s[0] != '0' and '.' not in s and s.isnumeric():
        print('YES')

    else:
        print('NO')
