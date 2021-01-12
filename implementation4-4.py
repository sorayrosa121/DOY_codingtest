'''
n, m = map(int, input().split())
x1, y1, direction = map(int, input().split())
visited = [[0] * m for _ in range(n)]
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
'''
#####

'''
o o o o
o x o o
o o o o
o o o o
(2x2) 자리에서 북쪽 바라보면 Front  BacK  Left  Right
                           (1,2)  (3,2) (2,1) (2,3) # x = [-1, 1, 0, 0], y = [0, 0, -1, 1] # -1 0
              서쪽          
                           (2,1)  (2,3) (3,2) (1,2) # x = [0, 0, 1, -1], y = [-1, 1, 0, 0] # 0 -1
              남쪽
                           (3,2)  (1,2) (2,3) (2,1) # x = [1, -1, 0, 0], y = [0, 0, 1, -1] # 1, 0
'''

m = 4
n = 4
data = [[1,1,1,1], [1,0,0,1], [1,1,0,1], [1,1,1,1]]
visited = [[0] * m for _ in range(n)]

x1, y1, direction = 1, 1, 0

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

index = direction
def turn_around():
    global index
    pass

def explore(data, x, y, visited):
    count = 0
    visited[x][y] = True # visited starting point

    nx = x + dx[direction]
    ny = y = dy[direction]

    if visited[nx][ny] == True or data[nx][ny] == 1: # if it already has been visited or is underwater, change direction
        turn_around()
    pass
    
    return count

array = [ [False] * 4 for _ in range(4) ]
array[1][1] = True
print(array)
