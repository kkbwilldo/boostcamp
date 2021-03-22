from sys import stdin

coin_arr = [500,100,50,10,5,1]

money = 1000 - int(stdin.readline())
answer = 0

    
for coin in coin_arr:
    if money >= coin:
        answer += money // coin
        money %= coin
        

print(answer)