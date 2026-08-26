'''
DFS - Depth first search
'''

def dfs( adlist , node , visited=None):
    #visited=None is used to ensure that a new set of visited nodes is created only when the function is first called.
    if visited is None:
        visited=set()
   
    if node not in visited:#checking for the node in visited set
        print(node, end=" ")
        visited.add(node) #marking as visited
        for neighbour in adlist[node]: #traversing the neighbours using adlist
            dfs(adlist,neighbour, visited)  #recursive call
            
graph = {
    1: [2,3],
    2: [1,5,6],
    3: [1,4,7],
    4: [3,8],
    5: [2],
    6: [2],
    7: [3,8],
    8: [4,7]
}

# Calling BFS from node 'A'
dfs(graph, 3)
            
    
            
    