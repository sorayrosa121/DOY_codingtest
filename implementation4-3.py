# possible moves
#      RRD, RRU, LLD, LLU, UUR, UUL, DDR, DDL
movex = [2, 2, -2, -2, 1, -1, 1, -1]
movey = [1, -1, 1, -1, -2, -2, 2, 2]

start = input()
def movement(start):
    count = 0 # how many moves
    y1, x1 = ord(start[0]) - ord('a') + 1, int(start[1]) # converts alphabet to number, str to int

    for i in range(len(movex)):
        nx = x1 + movex[i]
        ny = y1 + movey[i]
        
        if  nx > 8 or ny > 8 or nx < 1 or ny < 1: # as it should be in between (1,1) ~ (8,8)
            continue
        count += 1
    return count

print(movement(start))