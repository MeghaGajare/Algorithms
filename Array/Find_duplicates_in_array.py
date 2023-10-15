arr = list(map(int,input('enter elements:').strip().split()))

#with space

temp = []

for i in range(len(arr)):
    if arr[i] not in temp:
        temp.append(arr[i])
        print(temp)
    else:
        print('duplicate found at ',i,'index position with value ->',arr[i])
        