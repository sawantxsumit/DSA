'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
'''

#METHOD 1
#solving using recursive dfs

# def numberOfislands(grid):
#     if not grid:
#         return 0
    
#     row ,col= len(grid), len(grid[0])
#     island_count=0
    
#     def dfs(r,c):
#         #setting up the base condition
#         if r<0 or r>=row or c<0 or c>=col or grid[r][c]=='0':
#                 return
            
#         #mark as visited
#         grid[r][c]='0'
        
#         #visit in every direction
#         dfs(r+1,c)#down
#         dfs(r-1,c)#up
#         dfs(r,c+1)#right
#         dfs(r,c-1)#left
        
#     #iterate through all cells in grid
#     for r in range(row):
#         for c in range(col):
#             if grid[r][c]=='1':
#                 island_count+=1
#                 dfs(r,c)
         
#     return island_count
    
# grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]

# print(numberOfislands(grid))


#METHOD 2
#solving using iterative bfs

from collections import deque
def numberOfislands(grid):
    if not grid:
        return 0
    
    row,col= len(grid), len(grid[0])
    island_count=0
    
    def bfs(r,c):
        queue= deque([(r,c)])
        while queue:
            x,y=queue.popleft()
            if 0<= x <row and 0<= y <col and grid[x][y] =='1':
                grid[x][y]='0'
                queue.extend([(x+1,y),(x-1,y),(x,y+1),(x,y-1)])
        
    for r in range(row):
        for c in range(col):
            if grid[r][c]=='1':
                island_count+=1
                bfs(r,c)
                
    return island_count

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(numberOfislands(grid))
                