n = int(input())
for i in range(n):
    st = input()

    if st[0:len(st)] == st[::-1]:
        print('YES')

    else:
        print('NO')