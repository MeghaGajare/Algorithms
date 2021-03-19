# Largest Sum Contiguous Subarray
# Using Brute Force method
# time complexity : O(N^3)

array = list(map(int,input("Enter array Elements: ").strip().split()))
maxi = 0
for i in range(len(array)):
    for j in range(i,len(array)):
        
        sum = 0
        for k in range(i,j+1):
            sum += array[k]
            
        maxi = max(sum,maxi)
print("Brute Force method:-------------------------- ")
print("Largest Sum Contiguous Subarray",maxi)


# For time complexity: O(N^2)
maxi = 0
for i in range(len(array)):
    sum = 0
    for j in range(i,len(array)):

        sum += array[b]
        maxi = max(sum, maxi)
print("time complexity: O(N^2)")
print("Largest Sum Contiguous Subarray",maxi)







