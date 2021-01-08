def change(payment): # target amount
    answer = 0 # coin count
    coins = [500, 100, 50, 10] # types of coins, sorted
    for w in coins:
        answer += payment // w
        payment %= w

    return answer

print(change(1260))
