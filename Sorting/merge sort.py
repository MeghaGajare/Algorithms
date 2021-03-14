# Merge Sort
# time complexity : O(nlog(n))
def mergeSort(list):
    if(len(list)>1):
        mid = len(list)//2
        left = list[:mid]
        right = list[mid:]

        mergeSort(left)
        mergeSort(right)

        left_head,right_head,k = 0,0,0

        while(left_head<len(left) and right_head< len(right)):
            if(left[left_head]< right[right_head]):
                list[k] = left[left_head]
                left_head += 1
            else:
                list[k] = right[right_head]
                right_head +=1
            k +=1

        while(left_head < len(left)):
            list[k] = left[left_head]
            left_head +=1
            k +=1

        while(right_head < len(right)):
            list[k] = right[right_head]
            right_head += 1
            k += 1

li = list(map(int,input('Enter a list elements:').strip().split()))
(mergeSort(li))
print(li)        
