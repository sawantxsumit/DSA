'''
dynamic array
1. create list[D]
2. len
3. append
4. print
5. indexing
6. pop
7. clear 
8. find
9. insert
10. delete
11. remove
''' 

import ctypes

class Mylist:
    
    def __init__(self):
        self.size=1
        self.n=0
        #Create a C type array with size = self.size
        self.A=self.__make_array(self.size)
        
    def __len__(self):
        return self.n
    
    def __make_array(self,capacity):
        #creates a Ctype array [static, referential] with size capacity
        return (capacity*ctypes.py_object)()
    
    def append(self, item):
        if self.size== self.n:
            #resize
            self.resize_arr(self.size*2)
            
        #append
        self.A[self.n]= item
        self.n= self.n + 1
    
    def __str__(self):
        result=''
        for i in range(self.n):
            result=result + str(self.A[i] + "," )
        
        return '[' + result + ']'
    
    def resize_arr(self, new_capacity):
        #create a new array with new capacity
        B= self.__make_array(new_capacity)
        self.size= new_capacity
        #copy the content of A to B
        for i in range(self.n):
            B[i]=self.A[i]
        
        #reassign A
        self.A=B
    
    def __getitem__(self, index):
        if 0<= index < self.n:
            return self.A[index]
        else:
            return 'index out of range '
        
        
            
    
l= Mylist()
l=[10,20,30]
l.append("hello")
l.append(True)
l.append(100)
l.append(3.5)
print(l[7])

print(l)