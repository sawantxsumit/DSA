def linear_search(array, target):
    if not array:
        return
    for i in range(len(array)):
        if array[i]==target:
            return i
    return None

a=[2,3,5,4,3,44,34,233,2331,87,90]
b=[]
target=34
print('Target found at index :',linear_search(a,target))