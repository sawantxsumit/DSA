'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
'''
# def setZeroes(matrix):
#     rows = len(matrix)
#     cols = len(matrix[0])

#     # Step 1: Check if first row and first column need to be zeroed
#     first_row_has_zero = any(matrix[0][j] == 0 for j in range(cols))
#     first_col_has_zero = any(matrix[i][0] == 0 for i in range(rows))

#     # Step 2: Use first row and column as markers
#     for i in range(1, rows):
#         for j in range(1, cols):
#             if matrix[i][j] == 0:
#                 matrix[i][0] = 0  # Mark the row
#                 matrix[0][j] = 0  # Mark the column

#     # Step 3: Set cells to 0 using the markers
#     for i in range(1, rows):
#         for j in range(1, cols):
#             if matrix[i][0] == 0 or matrix[0][j] == 0:
#                 matrix[i][j] = 0

#     # Step 4: Zero the first row if needed
#     if first_row_has_zero:
#         for j in range(cols):
#             matrix[0][j] = 0

#     # Step 5: Zero the first column if needed
#     if first_col_has_zero:
#         for i in range(rows):
#             matrix[i][0] = 0

#brute force solution by me
def setZeroes(matrix):
    zeroes=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==0:
                zeroes.append([i,j])
                
    for n in zeroes:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][n[1]]=0
                matrix[n[0]][j]=0
        
matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeroes(matrix)
print(matrix)
