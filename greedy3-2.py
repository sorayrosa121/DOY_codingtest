import time
start_time = time.time()

n, m, k = map(int, input().split()) # list_length, addition_count, maximum_consecutive
numbers = [int(x) for x in input().split()] # N numbers duplicated & not sorted

numbers.sort(reverse=True)
first = numbers.pop(0) # biggest number
second = numbers.pop(0) # second biggest number



# First, place the biggest number. Then the second number in between
answer = first * k * (m // k) + second * (m % k)

print(answer)

print("---%s seconds ---" % (time.time() - start_time))
