    #!/bin/python3

import sys


s = input().strip()

if s[0:2]!='24':
    if s[len(s)-2] + s[len(s)-1] == 'PM':
        if s[0:2]=='12':
            print(s[0:len(s)-2])

        else:
            k = int(s[0:2]) + 12

            new_s = str(k) + s[2:len(s)-2]

            print(new_s)



    elif s[len(s)-2] + s[len(s)-1] == 'AM':
            if s[0:2]!='12':
                k = s[0:2]
                new_s1 = k + s[2:len(s) - 2]
                print(new_s1)
            elif s[0:2]=='12':
                k='00'
                n1=(k + s[2:len(s) - 2])
                print(n1)


    elif s == '12:00:00AM':
        print('00:00:00')



    elif s == '12:00:00PM':
        print('12:00:00')

else:
    k='00'
    n1=(k + s[2:len(s) - 2])
    print(n1)
