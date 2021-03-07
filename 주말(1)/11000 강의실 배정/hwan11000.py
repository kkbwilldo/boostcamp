from sys import stdin
from _collections import deque
import heapq

N = int(stdin.readline())
class_arr = sorted([list(map(int, stdin.readline().split())) for _ in range(N)],
                    key=lambda x:(x[1],x[0]))

queue = deque([class_arr[0][1]])
# queue = []
# heapq.heappush(queue, class_arr[0][1])

for i in range(1, N):
    
    start, end = class_arr[i]
    if start >= queue[0]:
        # heapq.heappop(queue)
        queue.popleft()
    # heapq.heappush(queue, end)
    queue.append(end)
    

print(len(queue))