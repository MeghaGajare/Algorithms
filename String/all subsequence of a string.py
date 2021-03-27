# print all subsequence of a string using recursion

##format=(input,output)
##example:
##                 [ ab,'' ]
##                /         \
##            [b,'' ]       [  b,'a']         #reject str[0]  then accept str[0]
##             /   \         /     \
##        ['',''] ['','b'] ['','a'] ['','ab']



def subsequence(string,op):
    if(len(string)==0):
        print(op)
        return
    subsequence(string[1:],op)                  #you can take : string[:-1],op
    subsequence(string[1:],op+string[0])        #you can take : string[:-1], op+string[-1]
    

a = input('Enter a string: ')

output = ""
subsequence(a,output)
