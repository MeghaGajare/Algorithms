#String is rotation of another

s1 = input('enter a string: ')
s2 = input('enter another string: ')

result = s1+s2 
if(len(s1) == len(s2)):
    if(s2 in result):
        print('strings are rotation of each other')
    else:
        print('strings are not rotation of each other')
else:
    print('length is not equal.')
