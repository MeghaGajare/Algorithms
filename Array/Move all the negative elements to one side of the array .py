arr = list(map(int,input("enter array elements negative to positive: ").strip().split()))
print(arr)
arr.sort()
print(arr)

for e in arr:
    print(e,end=' ')
