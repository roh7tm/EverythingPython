def capital(string):
    string = string[0].upper() + string[1:len(string)]
    return  string




string ='hello world wow '
ls = string.strip().split(' ')
s = ""

for i in range(len(ls)):
    if ls[i][0] != ' ' and not ls[i][0].isnumeric() and ls[i][0].islower():
        s = s + " " + capital(ls[i])

    else:
        s = s + " " + ls[i]


print(s)
