no_of_elements , rotations = input().strip().split(' ')
no_of_elements , rotations = [int(no_of_elements), int(rotations)]
k = []
ls = list(map(int,input().split(' ')))
k = ls[rotations:len(ls)]+ ls[0:rotations]
for num in range(len(k)):
    print(k[num],end=' ')