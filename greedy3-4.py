n, k = map(int, input().split()) # initial_number, divide_number
answer = 0 # calculation count

def minus(x):
    global answer
    answer += 1
    return x - 1

def divide(y, a):
    global answer
    answer += 1
    return y // a

def till_one(i, j):
    if i == 1:
        return answer
    elif i % j == 0:
        return till_one(divide(i, j), j)
    else:
        return(till_one(minus(i), j))
    
print(till_one(n, k))