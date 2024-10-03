def mergesort(a):
    if len(a)>1:
        mid=len(a)//2
        L=a[:mid]
        R=a[mid:]
        mergesort(L)
        mergesort(R)
        a.clear()
        while len(L)>0 and len(R)>0:
            if L[0]<=R[0]:
                a.append(L[0]) 
                L.pop(0) 
            else:
                a.append(R[0]) 
                R.pop(0) 
        for i in L:
            a.append(i)        
        for i in R:
            a.append(i)     
a=[24,6,8,15,2]      
mergesort(a)     
print(a)
