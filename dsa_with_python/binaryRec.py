class A():
    def binary_recur(self , low,high,list,x):
        if low>high:
            return -1
        mid=(low+high)//2
        if(list[mid]==x):
            return mid
        elif x>list[mid]:
            return self.binary_recur(mid+1,high,list,x)
        return self.binary_recur(low,mid-1,list,x)
        
                      
        
l=A()
num= [23,43,2,8,12,78,56,89,109]
num.sort() 
a=l.binary_recur(0,8,num,3)

print("The index of the element is :",a)