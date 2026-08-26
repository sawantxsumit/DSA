'''
BFS - Breadth first search

'''

from collections import deque

def bfs(adList , start_node):
    visited=set()   #making a set of visited elements  ( a set can't contain duplicate elements)
    queue= deque([start_node])  #adding start node in the queue 
    
    while queue:
        node= queue.popleft()  #dequeuing elements one by one
        if node not in visited:
            print(node , end=" ") #printing the nodes
            visited.add(node)   #marking as visited
            queue.extend(adList[node]) #adding neighbours to the queue one by one (can't use append here )
            
            
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Calling BFS from node 'A'
bfs(graph, 'A')
            