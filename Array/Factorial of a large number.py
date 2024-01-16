#Factorial of large numbers

##Input: N = 5
##Output: 120
##Explanation : 5! = 1*2*3*4*5 = 120

##Input: N = 10
##Output: 3628800
##Explanation :
##10! = 1*2*3*4*5*6*7*8*9*10 = 3628800


num = int(input("Enter a value: "))

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact* i
        print(i,'*',fact,end='\n')
    print()
    return fact

print('Factorial of large numbers: ',factorial(num))





