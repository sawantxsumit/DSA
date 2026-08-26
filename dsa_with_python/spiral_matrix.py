'''
Given an m x n matrix, return all elements of the matrix in spiral order.
Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]


algorithm used:
when moving in right direction i(same) j=j+1
when moving in left direction i(same) j=j-1
when moving in up direction j(same) i=i-1
when moving in down direction j(same) i=i+1

while moving in a sprial the path will be right down left up and again same until matrix is finished
'''

# class Solution(object):
#     def spiralOrder(self, matrix):
#         #check if the matrix is empty or not
#         if not matrix or not matrix[0]:
#             return []
        
#         m=len(matrix)
#         n=len(matrix[0])
#         result=[]
        
#         top , bottom , left , right = 0,m-1, 0, n-1
#         while top <= bottom and left <= right:
#         # Move right
#             for j in range(left, right + 1):
#                 result.append(matrix[top][j])
#             top += 1
            
#             # Move down
#             for i in range(top, bottom + 1):
#                 result.append(matrix[i][right])
#             right -= 1
            
#             if top <= bottom:
#                 # Move left
#                 for j in range(right, left - 1, -1):
#                     result.append(matrix[bottom][j])
#                 bottom -= 1
            
#             if left <= right:
#                 # Move up
#                 for i in range(bottom, top - 1, -1):
#                     result.append(matrix[i][left])
#                 left += 1
        
#         return result
        
class Solution():
    def spiralOrder(self , matrix):
        if not matrix or not matrix[0]:
            return matrix
        top=left=0
        bottom=len(matrix)-1
        right=len(matrix[0])-1
        result=[]
        
        while  top<=bottom and left<=right:
            #move right
            for i in range(left , right+1):
                result.append(matrix[top][i])
            top+=1
            
            #move down
            for i in range(top , bottom+1):
                result.append(matrix[i][right])
            right-=1
            
            if top<=bottom:
                #move left
                for i in range(right,left-1,  -1):
                    result.append(matrix[bottom][i])
                bottom-=1
                
            if left<=right:
                #move  up
                for i in range(bottom , top-1 , -1):
                    result.append(matrix[i][left])
                left+=1
                             
        return result
l=Solution()
num=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
res=l.spiralOrder(num)
print(res) 

  

