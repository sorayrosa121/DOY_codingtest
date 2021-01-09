n, m = map(int, input().split()) # row, column (n x m)
array = []

for i in range(n):
    array.append(list(map(int, input().split()))) # 2D array [ [], [], [] ]

temp_compare = []
for index, each_row in enumerate(array):
    temp_compare.append((min(each_row), index))
print(temp_compare)
temp_compare.sort(reverse=True)

print(temp_compare[0][0])