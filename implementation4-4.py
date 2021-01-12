'''
n, m = map(int, input().split()) # (n x m)
# direction = [0 , 1, 2, 3]
#               N, E, S, W
x1, y1, direction = map(int, input().split()) # starting point: (1,1), direction: 0
visited = [[False] * m for _ in range(n)]
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
'''
#####

'''
o o o o o
o o o o o
o o x o o
o o o o o
o o o o o

from (2x2) heading North:  Front  BacK  Left  Right
                           (1,2)  (3,2) (2,1) (2,3)  ## x = [-1, 1, 0, 0], y = [0, 0, -1, 1] # -1 0
                    West:          
                           (2,1)  (2,3) (3,2) (1,2)  ## x = [0, 0, 1, -1], y = [-1, 1, 0, 0] # 0 -1
                   South:
                           (3,2)  (1,2) (2,3) (2,1)  ## x = [1, -1, 0, 0], y = [0, 0, 1, -1] # 1, 0
'''

m = 4
n = 4
data = [[1,1,1,1], [1,0,0,1], [1,1,0,1], [1,1,1,1]]
visited = [[False] * m for _ in range(n)]

# direction = [0 , 1, 2, 3]
#               N, E, S, W
x1, y1, direction = 1, 1, 0 # starting point: (1,1), direction: 0

dx = [-1, 0, 1, 0] # N W S E != direction
dy = [0, -1, 0, 1]

# direction = 3 -> ndirection = 2
# direction = 2 -> ndirection = 1
# direction = 1 -> ndirection = 0
# direction = 0 -> ndirection = 3

count = 1 # include starting point
turned = 0

def turn_around():
    global direction
    global turned
    direction -= 1
    turned += 1
    if direction == -1:
        direction = 3

def explore(data, x, y, visited):
    global count
    global turned
    while True:
        visited[x][y] = True # visited starting point

        if turned == 4:
            nx = x - dx[direction]
            ny = y - dy[direction]
            if data[nx][ny] == 1:
                break
            x, y = nx ,ny
            turned = 0

        nx = x + dx[direction]
        ny = y = dy[direction]

        if visited[nx][ny] == True or data[nx][ny] == 1: # if it already has been visited or is underwater, Change direction
            turn_around()
            explore(data, x, y, visited)
        x, y = nx, ny
        count += 1
        turned = 0
        
    return count

print(explore(data, x1, y1, visited))