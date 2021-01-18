### filling ice cube trays
# 0: empty
# 1: blocked
n, m = map(int, input().split()) # n row x m column
graph = [list(map(int, input())) for _ in range(n)]

def dfs(x, y):
    if x < 0 or y < 0 or x > n-1 or y > m-1 : # if beyond the scope (0, 0) ~ (n-1, m-1)
        return False
    if graph[x][y] == 0: # if it's not blocked
        graph[x][y] = 1 # fill it in
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True # means it created a piece of ice
    return False

count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count += 1
print(count)
