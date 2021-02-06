### till one

d = [0] * 30001 # not 30000 as index starts from 0
x = int(input())
for i in range(2, x+1):
    d[i] = d[i-1] +1 # minus 1 is available with NO condition
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] +1)
        
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] +1)
        
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] +1)
        
print(d[x])