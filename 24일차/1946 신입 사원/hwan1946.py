from sys import stdin
import heapq


for _ in range(int(stdin.readline())):

    N = int(stdin.readline())
    num_arr = [list(map(int, stdin.readline().split())) for _ in range(N)]
    heapq.heapify(num_arr)
    temp = heapq.heappop(num_arr)[1]
    answer = 1
    # print('-------------------')
    while num_arr:
        chk = heapq.heappop(num_arr)

        # print(temp, chk[1])
        # print('---')
        if temp < chk[1]:
            pass
        else:
            temp = min(temp, chk[1])
            answer += 1
        
    print(answer)