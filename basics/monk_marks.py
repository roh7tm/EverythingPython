array_size , max_score = input().strip().split(' ')
array_size , max_score = [int(array_size), int(max_score)]

monk_mark = [ int(x) for x in input().split(' ')]
skip = 0
count = 0
for i in range(len(monk_mark)):

    if monk_mark[i] <= max_score:
        count = count + 1

    elif skip==0:
        skip +=1

    else:
        break

print(count)

