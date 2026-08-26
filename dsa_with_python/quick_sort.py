def quick_sort( a :list , low , high)-> list :
    if not a:
        return 0
    if len(a)==1:
        return a
    pivot=a[0]
    i=1 , j=len(a)-1
    for i , j in range(len(a)):
        if a[i]<pivot:
            i+=1
        if a[j]>pivot:
            j-=1
        if i>j:
            
            
        
    