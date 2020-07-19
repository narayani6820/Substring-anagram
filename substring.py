import enchant
d = enchant.Dict("en_US")
def subString(s,n):
    
    temp =[]
    for i in range(n): 
        for len in range(i+1,n+1): 
           temp.append (s[i: len]);
    return temp
  
  
def permutation(elements):
    if len(elements) <=1:
        return elements
    else:
        tmp =[]
        for perms in permutation(elements[1:]):

            for i in range(len(elements)):
                tmp.append(perms[:i] + elements[0:1] + perms[i:])
        return tmp
list =[]
list1 =[]
list2 =[]
list=permutation("funeral")
for i in list:
    if(d.check(i)):
        print(i)
list1 = subString("funreal",len("funreal"))
for j in list1:
    if(len(j)>1 and j!="funeral"):
        list2=permutation(j)
        for j in list2:
            if(d.check(j)):
                print(j)
        
        


