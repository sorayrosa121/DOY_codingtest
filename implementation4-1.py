n = int(input()) #(n x n)
instruction = input().split() #which direction to travel

x, y = 1, 1 #initial x,y coordinate

def direction(next_sign):
    global x, y
    print(next_sign, x, y)
    # should be in between (1,1) ~ (n,n)
    if next_sign == 'L' and y > 1:
        y -= 1
    elif next_sign == 'R' and y < n:
        y += 1
    elif next_sign == 'U' and x > 1:
        x -= 1
    elif next_sign == 'D' and x < n:
        x += 1
            
for signs in instruction:
    direction(signs)

print(x, y)