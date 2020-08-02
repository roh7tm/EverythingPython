s = 'sadw96aeafae4awdw2wd100awd'
i = 0
k = 0
c = 0
flag= True
while i < len(s)-2:
    if s[i].isnumeric():
         k = i+1
         while s[k].isnumeric():
             k = k+1
             flag = False

         i = k
    elif s[i].isalpha():
        k = i + 1
        while s[k].isnumeric():
            k = k+1
            flag = True

    if flag == False:
        c = c+1

    i = k

print(c)

