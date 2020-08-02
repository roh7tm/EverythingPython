import sys
for line in sys.stdin.readlines():
    a = line.split('//')
    a[0] = a[0].replace('->', '.')
    print('//'.join(a), end='')

