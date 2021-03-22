from sys import stdin
stdin = open("input.txt","r")
n , m = map(int,stdin.readline().split())
cards = list(map(int,stdin.readline().split()))

import heapq as hq
hq.heapify(cards)

for _ in range(m):
    x=hq.heappop(cards)
    y=hq.heappop(cards)
    hq.heappush(cards,x+y)
    hq.heappush(cards,x+y)

print(sum(cards))