class A():
    def binary_search(self , list,x):
        n=len(list)
        print(list)
        low,high=0,n-1
        while(low<=high):
            mid=(low+high)//2
            if(list[mid]==x):
                return mid
            elif(x>list[mid]):
                low=mid+1
            else:
                high=mid-1
        return -1
            
        
l=A()
num= [23,43,2,8,12,78,56,89,109]
num.sort() 
a=l.binary_search(num,109)

print("The index of the element is :",a)