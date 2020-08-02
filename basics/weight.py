d = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
word = "apple"
sums = 0
for i in range(len(word)):
    sums += d[word[i]]
print(sums)
'''
cal = []
s = "abccddde"
c = 1
for j in range(len(s)-1):
    if s[i] == s[i+1]:
        c = c+1
        print(c)
    else:
        c = 1
    cal = cal + [d[s[i]]*c]

print(cal)
'''