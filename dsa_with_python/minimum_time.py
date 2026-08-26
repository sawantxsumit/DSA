'''
On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in seconds to visit all the points in the order given by points.

You can move according to these rules:

In 1 second, you can either:

move vertically by one unit,
move horizontally by one unit, or
move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).

You have to visit the points in the same order as they appear in the array.

You are allowed to pass through points that appear later in the order, but these do not count as visits.
'''

class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        time=0
        x1,y1=points.pop()
        while points:
            x2,y2= points.pop()
            time += max(abs(x2-x1), abs(y2-y1))
            x1,y1=x2,y2
        return time

l=Solution()
num=[[3,2],[-2,2]]
res=l.minTimeToVisitAllPoints(num)
print(res)   