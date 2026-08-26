'''
Given two sorted arrays a[] and b[], where each array may contain duplicate elements , the task is to return the elements in the union of the two arrays in sorted order.

Union of two arrays can be defined as the set containing distinct common elements that are present in either of the arrays.
Examples:

Input: a[] = [1, 2, 3, 4, 5], b[] = [1, 2, 3, 6, 7]
Output: 1 2 3 4 5 6 7
'''

def union(a, b):
    a.sort()
    b.sort()
    c=a+b
    c.sort()
    u=set(c)
    return u
    
a= [1, 2, 3, 4, 5]
b= [1, 2, 3, 6, 7]
print(union(a,b))