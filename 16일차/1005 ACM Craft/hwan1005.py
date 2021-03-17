from sys import stdin
from _collections import defaultdict, deque

T = int(stdin.readline())

for _ in range(T):
    
    N, K = map(int, stdin.readline().split())
    D = [0] + list(map(int, stdin.readline().split()))
    
    sequence = [0] * (N+1)
    indegree = [0] * (N+1)
    adjList = [[] for _ in range(N+1)]

    for _ in range(K):
        x, y = map(int, stdin.readline().split())
        indegree[y] += 1
        adjList[x].append(y)
    
    end_building = int(stdin.readline())

    dq = deque()
    for i in range(1, N+1):
        if not indegree[i]:
            sequence[i] = D[i]
            dq.append(i)

    for _ in range(N):
        if not dq:
            break

        target = dq.popleft()

        for x in adjList[target]:
            sequence[x] = max(sequence[x], sequence[target] + D[x])
            indegree[x] -= 1

            if not indegree[x]:
                dq.append(x)
    
    # print(sequence)
    # print(f'answer : {sequence[end_building]}')
    print(sequence[end_building])
