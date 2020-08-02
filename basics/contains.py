q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    n = len(s)
    word = 'hackerrank'
    m = 0
    j = 0
    for i in range(n):
        if s[i] == word[j]:
            j += 1
            m = m+1


        if j >= len(word):
            break

    if m == 10:
        print('YES')

    else:
        print('NO')
