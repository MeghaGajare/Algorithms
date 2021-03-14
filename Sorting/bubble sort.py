#Bubble sort in python

#complexity: O(n^2)
a = list(map(int,input().strip().split()))
for i in range(len(a)):
    for j in range(len(a)-1-i):
        if(a[j]>a[j+1]):
            a[j],a[j+1] = a[j+1],a[j]

print('Sorted array: ',a)
