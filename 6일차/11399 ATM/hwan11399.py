from sys import stdin
import heapq

N = int(stdin.readline())

heap = list(map(int, stdin.readline().split()))
heapq.heapify(heap)

answer = 0
before_val = 0

while heap:
    time = heapq.heappop(heap)
    before_val += time
    answer += before_val
    
print(answer)