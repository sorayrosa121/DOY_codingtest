### making  m KRW with n smaller bills

n, m = map(int, input().split()) # number of bill type, target amount
array = [] # each bill value
for _ in range(n):
    array.append(int(input()))

INF = 10e9
d = [INF] * (m+1)

d[0] = 0 # possible if none were used

for i in range(n):
    for j in range(array[i], m+1):
        if d[j - array[i]] != INF:
            d[j] = min(d[j], (d[j - array[i]] + 1))

if d[m] == INF:
    print(-1)
else:
    print(d[m])