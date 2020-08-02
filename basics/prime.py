n = 59
c = 0
for i in range(1,58):
    if n % i == 0:
        c = c+1


if c == 2:
    print('prime')
