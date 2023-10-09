a = list(map(int,input("enter element of Array A:").strip().split()))
b = list(map(int,input("enter element of Array B:").strip().split()))

size_a = len(a)
size_b = len(b)
i,j = 0,0

a.sort()
b.sort()

def union(a,b,size_a,size_b):
    i,j = 0,0
    while i<size_a and j<size_b:
        if (a[i]<b[j]):
            print(a[i],end = ' ')
            i+=1
        elif (a[i]>b[j]):
            print(b[j],end = ' ')
            j+=1
        else:
            print(b[j],end=' ')
            i+=1
            j+=1

    while i<size_a:
        print(a[i],end=' ')
        i+=1
    while j<size_b:
        print(b[j],end=' ')
        j+=1

def union2(a,b,size_a,size_b):
    temp = []
    if(size_a>size_b):
        temp = a
        for i in b:
            if(i in temp):
                pass
            else:
                temp.append(i)
    else:
        temp = b
        for i in a:
            if(i in temp):
                pass
            else:
                temp.append(i)
    print('union2 Final:',temp)

            

union2(a,b,size_a,size_b)