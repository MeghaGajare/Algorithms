arr = [31,5,67,8,1,3,93,3,200]
print("before sorting:",arr)
arr.sort()
print("after sorting:",arr)

print('Maximum value :',min(arr))
print("Minimum value :",max(arr))

print("-------------Min-Max-----------------")

mini,maxi = arr[0],arr[1]
def getMinMax(arr,mini,maxi):
    
    for i in range(2,len(arr)):
        
        if arr[i] > maxi:
            maxi = arr[i]
        elif arr[i] < mini:
            mini = arr[i]
    return mini,maxi

n,x = getMinMax(arr,mini,maxi)

print('min : ',n)
print('max : ',x)
