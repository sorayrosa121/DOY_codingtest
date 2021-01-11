# time hh:mm:ss
n = int(input()) # n:59:59
count = 0 # how many '3's
for hour in range(n+1): # 0 ~ n hour
    for minute in range(60): # 00 ~ 59 minute
        for second in range(60): # 00 ~ 59 second
            print(str(hour) + str(minute) + str(second))
            if '3' in str(hour) + str(minute) + str(second):
                count += 1
print(count)