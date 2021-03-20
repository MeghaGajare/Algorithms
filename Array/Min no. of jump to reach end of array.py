# minimum numbers of jumps to reach end of the array


#[1 1 2 3 2 1 0 0 1 3]
#reachable indexes: 0,1,2,4,6  -----we can't move ahead
# so maximum reachable index is 6
# In this case reachable index < current index then return 'false'


ar = list(map(int,input().strip().split()))


def minimumJump(ar):
    reachable = 0
    step,jump = ar[0],0
    for i in range(len(ar)):
        if(ar[0]== 0 or ar[0]<0):   # case: [0 3 3]
            return "Not possible to reach."
        
        elif(reachable < i):
            return "Not possible to reach."

        if(i == len(ar)-1):          #At the end of the index
            return jump             #stop jumping
        
        reachable = max(reachable, i+ar[i])  #maximum reach in array
        step -= 1                            #get current index

        if(step == 0):              #No step left
            jump +=1                #let's jump
            step = reachable - i    #reinitialize the steps 
        
    return "Not possible to reach."

print("Minimum jump is : ",minimumJump(ar))
