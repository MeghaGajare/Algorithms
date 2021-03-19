# coin change problem using dynamic programming

# find the minimum no of coins to make change of given amount using given coin.
coins= list(map(int,input('enter a coins: ').strip().split()))
amount= int(input("Enter a amount(int): "))

def printlist(a):
    for i in a:
        print(i)
    print()

def MinCoins(coins,amount):
    a = [[0 for i in range(amount+1)] for j in range(len(coins)+1)]
    printlist(a)
    for i in range(len(coins)+1): #0,1,2,3
        a[i][0]=1
    for i in range(len(coins)+1): #0,1,2,3
        for j in range(amount+1): #0 1 2 3 4 5
            if(coins[i]>j):
                a[i][j]= a[i-1][j]
            else:
                a[i][j]= min((a[i-1][j],1+a[i][j-coins[i]]))
               # printlist(a)
    printlist(a)
    return a[len(coins)-1][amount-1]

print(MinCoins(coins,amount))
