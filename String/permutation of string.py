#permutation of a string
##                      [ABC] ---------------------level 1
##            [ABC]     [BAC]      [CBA]-----------level 2
##         [ABC][ACB] [BAC][BCA] [CBA][CAB]--------level 3
##----------------------------------------------------------------
#therfore, (length(str)== heigth) -->

##Important:-
##1))decreasing no of branches as we move downword
##2))At each level no of branches decrease by 1

##time complexity:-
##O([time to print 1 permutation] * [no of permutation])

##logic:
##    swap
##    permute recursion call
##    swap 

from itertools import permutations

#----------------------xxxxxxxxxxxxxxxxxxx------------------------------------------
def str_to_list(string): #--------string to list
    li=[]
    li[:0]=string
    return li

def swap(a,b):
    temp = a
    a=b
    b=temp
#----------------------xxxxxxxxxxxxxxxxxxx------------------------------------------
s = input('enter a string: ')
permuted = []
def permutation(string,l,r):  
    if(len(string)==l):
        permuted.append(''.join(string))
    else:
        for i in range(l,r):
            string[l],string[i]= string[i],string[l]       # eg. ab -> ba
            permutation(string,l+1,r)                      #recursion call
            string[l],string[i]= string[i],string[l]       #backtracking eg. ba->ab

permutation(list(s),0,len(s))
print(str(permuted))

#----------------------------------------------------------------

s1 = input('enter a string: ')
result = []
for i in permutations(s1):
    result.append(''.join(i))
print('permutaitons: ',result)
























            
