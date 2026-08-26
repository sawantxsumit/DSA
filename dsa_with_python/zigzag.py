'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
'''
#method 1 -> neetcode
#time complexity will be length of the string
# def zigzag(s, numRows):
#     if numRows==1:
#         return s
#     res=''
#     for r in range(numRows):
#         increment=2*(numRows-1)
#         for i in range(r, len(s), increment):
#             res+=s[i] #this condition is meant for first and last row only all other will follow the condition below
#             if r>0 and r<numRows-1 and i+increment-2*r < len(s):
#                 res+= s[i+increment-2*r]
#     return res

#method 2 -> GPT
'''Imagine this:
You have 3 stairs (or 3 lines), and you want to write a message like "PAYPALISHIRING" by going down the stairs and up again, over and over.

Here’s how the message is written:
Step 1 (down):   P
Step 2 (down):   A
Step 3 (down):   Y
Step 2 (up):     P
Step 1 (up):     A
Step 2 (down):   L
Step 3 (down):   I
Step 2 (up):     S
Step 1 (up):     H
... and so on!
'''
def zigzag( s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s
    
    rows = [''] * numRows
    curRow = 0
    goingDown = False
    
    for char in s:
        rows[curRow] += char
        # Reverse direction if we reach the top or bottom
        if curRow == 0 or curRow == numRows - 1:
            goingDown = not goingDown

        if goingDown:
            curRow+=1
        else:
            curRow-=1
    return ''.join(rows)

                
                
    
s='paypalishiring'
n=4
res=zigzag(s,n)
print(res)