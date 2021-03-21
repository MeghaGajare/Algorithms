#duplicate characters in string

s = input('enter a string: ')
char = []
duplicates = []
for i in s:
    if(i not in char):
        char.append(i)
    else:
        duplicates.append(i)
print('duplicates characters: ',list(set(duplicates)))



#count frequencies of characters
dic = dict()
for i in s:
    if(i not in dic):
        dic[i]= 1
    else:
        dic[i]+=1

for keys in dic:
    print(keys,':',dic[keys])







    
