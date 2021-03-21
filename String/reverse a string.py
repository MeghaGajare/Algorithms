#reverse a string

string = input()
a = string[::-1]
print('reverse string: ',a)

# or
b = ''
for i in string:
    b=i+b
print(b)

#check palindrome string
if(a == string):
    print("It is a palindrome.")
else:
    print("It is not palindrome.")
