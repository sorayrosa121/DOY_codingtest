### maze escape
# 0: where the monter stays; can't travel
# 1: possible route

from collections import deque
n, m = map(int, input().split()) # n row x m column
graph = [list(map(int, input())) for _ in range(n)]

# direction
dx = [1, -1, 0, 0] # down, up, right, left 
dy = [0, 0, 1, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y)) # deque([(x, y)]) would work the same
    while queue:
        x, y = queue.popleft()
        for i in range(4): # four direction
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx > n-1 or ny > m-1: # if beyond the scope (0, 0) ~ (n-1, m-1)
                continue
            if graph[nx][ny] == 0: # if there's a monster
                continue
            if graph[nx][ny] == 1: # if it hasn't been traveled
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]

print(bfs(0, 0))