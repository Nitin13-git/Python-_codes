# we have to chick wheather 0 is present id not or yes
'''def  check0(L):
    if len(L)==0:
        return 0
    elif L[0]==0:
        return 1
    else:
        return check0(L[1:len(L)])

print(check0([1,23,432,43,66]))'''

'''def mini(L):
    minimum=L[0]
    for i in range (len(L)):
        if L[i]<minimum:
            minimum=L[i]
    return minimum

def sort(L):
    if len(L)==0 or len(L)==1:
        return L
    m=mini(L)
    L.remove(m)
    return [m]+sort(L)
L=[2,18,3,5453,44,356,33,456]
print(sort(L))

'''
'''def obious_search(L,k):
    for i in range(len(L)):
        if L[i]==k:
            return 1
    return 0

l=list(range(100))
print(obious_search(l,14))'''
import time
a=time.time()
def binary_search(L,k):
    begin=0
    end=len(L)-1
    while (end-begin>1):
        mid=(end-begin)//2
        if L[mid]==k:
            return 1

        if L[mid]>k:
            end=mid-1
        if L[mid]<k:
            begin=mid+1
    
    if (L[begin]==k) or (L[end]==k):
        return 1
    else:
        return 0
L=list(range(1000000))
print(binary_search(L,-1))
b=time.time()
print(b-a)






