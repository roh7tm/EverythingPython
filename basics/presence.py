def count_it(ls):
    st = 'AEIOUaeiou'
    c = 0
    for i in range(len(ls)):
        for character in ls[i]:
            if character in st:
                c = c + 1
        return c




n = 5
ls=[]
while n > 0:

    ls = ls + [x for x in input().strip().split('\n')]
    n = n-1

print(count_it(ls))
print(ls)