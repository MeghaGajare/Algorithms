# kadane's algorithm
# time complexity: O(N)

ar = list(map(int,input("Enter array elements: ").strip().split()))

sum = 0
maxi = ar[0]    #init with 1st element
for i in range(len(ar)):
    sum += ar[i]
    if(sum > maxi):
        maxi = sum
    if(sum < 0):
        sum = 0
print('Largest sum contiguous subarray: ',maxi)




