from sys import stdin
import heapq
from copy import deepcopy

N, K = map(int, stdin.readline().split())


jewerly = [list(map(int, stdin.readline().split())) for _ in range(N)]
bag = [int(stdin.readline()) for _ in range(K)]

heapq.heapify(jewerly)
heapq.heapify(bag)


answer = 0
candidate = []

while bag:
    weight = heapq.heappop(bag)
    
    while jewerly and weight >= jewerly[0][0]:
        jew_w, jew_c = heapq.heappop(jewerly)
        heapq.heappush(candidate, -1 * jew_c)
        
    
    if candidate:
        chk_cost = heapq.heappop(candidate)
        answer += chk_cost
        

    if not candidate and not jewerly:
        break

print(answer * -1)
    