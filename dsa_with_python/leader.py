# brute force approach -> o(n^2) complexity
# def leader(arr):
#     is_leader=[True]*len(arr)
#     for j in range(len(arr)):
#         for i in range(j):
#             if arr[j]>arr[i]:
#                 is_leader[i]=False
#     return is_leader

# a=[50,40,45,10,16,30]
# print(leader(a))

# Best approach
def leader(arr):
    leaders=[]
    n=len(arr)
    max_from_right=arr[-1]
    leaders.append(max_from_right) # Rightmost element is always the leader
    for i in range(n-2,-1,-1):
        if arr[i]> max_from_right:
            # if the current element is greater than the max_from_right
            leaders.append(arr[i]) 
            # update the value of max_from_right
            max_from_right=arr[i]

    leaders.reverse()
    return leaders

a=[50,40,45,10,16,30]
print(leader(a))

