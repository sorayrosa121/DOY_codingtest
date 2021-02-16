### from A to K to X

n, m = map(int, input().split())
INF = 1e9
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

x, k = map(int, input().split())

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)

'''
# 2차원 리스트 확인
for a in range(1, n+1):
    for b in range(1, n+1):
        print(graph[a][b], end = " ")
    print("\n")
'''