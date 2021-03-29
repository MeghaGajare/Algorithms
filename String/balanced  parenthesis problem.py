#check balanced parenthesis problem

open_bkt = ['{','(','[']
close_bkt = ['}',')',']']

string = input('enter a string: ')

stack = list()

def checkParenthesis(string,stack):
    
    if(len(string)>0):
        for i in string:
            if(i in open_bkt):
                stack.append(i)
            elif(i in close_bkt):
                location = close_bkt.index(i)
                if(len(stack)> 0 and stack[len(stack)-1]== open_bkt[location]):
                    stack.pop()
                else:
                    print('invalid')
                    return
            else:
                pass
        if(len(stack)==0):
            print('balanced')
            return
        else:
            print('unbalanced')
            return

checkParenthesis(string,stack)
