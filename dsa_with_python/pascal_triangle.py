'''
Given an integer numRows, return the first numRows of Pascal's triangle.
Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
'''
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     f=1
#     for i in range(2,n+1):
#         f=f*i
#     return f

# def combination(n,r):
#     return int(fact(n)/(fact(n-r)*fact(r)))

# def pascal(numRows):
#     triangle=[]
#     for i in range(numRows):
#         triangle.append([combination(i,j) for j in range(i+1)])
#     return triangle
        
#method 2 -> chat GPT
def pascal(numsRows):
    triangle = []

    for i in range(numRows):
        # Start each row with 1
        row = [1] * (i + 1)

        # Fill in the middle values using the previous row
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle

numRows = 3
a=pascal(numRows)
print(a)
  