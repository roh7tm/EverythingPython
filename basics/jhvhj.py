n = int(input())

for i in range(n):
    flag= False
    num = int(input())
    num_str = str(num)
    k = '21'
    if num % 21 == 0:
        print("The streak is broken!")
        flag=True

    if flag==False:
        for l in range(len(num_str)):
            if num_str[l:l + 3] == k:
                print("The streak is broken!")
                flag=True

    if flag==False:
        print("The streak lives still in our heart!")