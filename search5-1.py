### DFS vs. BFS

graph= [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
    ]
visited = [False] * 9

stack = []
def dfs(graph, v, visited):
    global stack
    visited[v] = True    
    if v not in stack:
        stack.append(v)
    for next_node in graph[v]:
        if not visited[next_node]:
            stack.append(next_node)
            dfs(graph, next_node, visited)
dfs(graph, 1, visited)
print(stack)

from collections import deque
graph= [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
    ]
visited = [False] * 9

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        now = queue.popleft()
        print(now, end= ' ')
        for i in graph[now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(graph, 1, visited)