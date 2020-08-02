'''
Input Format

A single integer, n, denoting the size of the staircase.

Output Format

Print a staircase of size n using # symbols and spaces starting from right side

  
    #
   ##
  ###
 ####

'''


n = int(input())

for i in range(1,n+1):
    print(" "*(n-i) + "#"*i)

'''



Input Format

A single integer, n, denoting the size of the staircase.

Output Format

Print a staircase of size n using # symbols and spaces starting from left side


    #
    ##
    ###
    ####
    
    n = int(input())

for i in range(1,n+1):
    print( "#"*i + " "*(n-i) )


'''

