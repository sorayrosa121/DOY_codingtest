### descending

n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

# sol.1) selection sort
for i in range(n):
    max_index = i
    for j in range(i+1, n):
        if array[max_index] < array[j]:
            max_index = j
            array[max_index], array[i] = array[i], array[max_index]

for i in array:
    print(i, end= ' ')

# sol.2) insertion sort
for i in range(n):
    for j in range(i, 0, -1):
        if array[j] > array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

for i in array:
    print(i, end= ' ')

# sol.3) sort() func.
array.sort(reverse=True)

for i in array:
    print(i, end= ' ')