# Buy and sell stock to get more profit

# buy -> sell

arr = [7,1,5,3,6,4]   # [7,6,4,3,1]

mini = arr[0]
profit = 0
for i in range(len(arr)):
    difference = arr[i] - mini
    profit = max(profit,difference)
    mini = min(mini,arr[i])
    # print("difference : ",difference," Profit: ",profit," mini: ",mini)
    print("Buy on day ",arr.index(mini)+1," Sell on day",arr.index(arr[i])," Profit : ",profit)

    # if(profit > 0):
    #     print("Buy on day ",arr.index(mini)+1,"(price = ",mini,") and sell on day ",arr.index(arr[i])," (price = ",arr[i],"), profit = 6-1 = 5")
    # else: 
    #     print("In this case, no transactions are done and the max profit = ",profit)

print("Profit: ",profit)
