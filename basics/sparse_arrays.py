no_of_word = int(input())
ls =[]
c = 0
for i in range(no_of_word):
    ls = ls + [input()]

no_of_qu = int(input())

for k in range(no_of_qu):
    query = input()
    for j in range(len(ls)):
        if query == ls[j]:
            c = c+1

    print(c)
    c = 0