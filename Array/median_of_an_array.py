a = [1,3,5]   #[2,10,12,26]
b = [2,4,6]   #[3,6,30,78,90]
print(a+b)

c = a+b
c.sort()
print(c)

length = len(c)
print(length)
print('half:',length/2)
val = length//2

if (length%2 != 0):
    print('median element of index: ',val,'=',c[val])
else:
    result=(c[val]+c[val-1])/2
    print('median element: ',result)
