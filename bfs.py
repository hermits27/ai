def bfs(graph, start):
    visited = [False] * len(graph)
    queue = []
    
    visited[start] = True
    queue.append(start)
    
    while queue:
        vertex = queue.pop(0)  # dequeue from front
        print(vertex, end=' ')
        
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

# Example graph as adjacency list (nodes are integers)
graph = [
    [1, 2],    # neighbors of 0
    [3, 4],    # neighbors of 1
    [5],       # neighbors of 2
    [],        # neighbors of 3
    [5],       # neighbors of 4
    []         # neighbors of 5
]

print("BFS traversal:")
bfs(graph, 0)
