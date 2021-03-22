from sys import stdin
import heapq

n, m = map(int, stdin.readline().split())

num_arr = list(map(int, stdin.readline().split()))

heapq.heapify(num_arr)

for _ in range(m):

    x, y = heapq.heappop(num_arr), heapq.heappop(num_arr)

    heapq.heappush(num_arr,x+y)
    heapq.heappush(num_arr,x+y)

print(sum(num_arr))