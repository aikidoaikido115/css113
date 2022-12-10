from collections import deque
graph = {
    "A":["B", "C", "E"],
    "B":["A", "C", "D"],
    "C":["A", "B", "D", "E"],
    "D":["B", "C", "E", "F", "G"],
    "E":["A", "C", "D", "G"],
    "F":["D", "G"],
    "G":["D", "E", "F"]
}
def bfs(g, root):
    queue = deque([root])
    visited = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            
        for item in g[node]:
            if item not in visited:
                queue.append(item)
    print(visited)
print ("-----------------------------------------------------------------------\
    \nBreadth First Search BFS for a Spanning Tree with Python Implementation")
bfs(graph, 'A')
print("-----------------------------------------------------------------------")


'''
ref: https://www.youtube.com/watch?v=CnECo0rUbzo     
'''
