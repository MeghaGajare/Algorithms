arr = list(map(int,input('enter elements:').strip().split()))

#with space

temp = []

for i in range(len(arr)):
    if arr[i] not in temp:
        temp.append(arr[i])
        print(temp)
    else:
        print('duplicate found at ',i,'index position with value ->',arr[i])

# the above code will increase space  complexity. to avoid use below 
duplicate = False
for i in range(len(arr)):
    for j in range(1,len(arr)):
        if(arr[i]==arr[j] and (i != j)) :
                duplicate = True
                print('duplicate found at position',j,'value: ',arr[j])
                break
        else:
             continue

if(duplicate == False):
     print("No duplicate Found")
