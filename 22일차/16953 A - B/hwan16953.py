from sys import stdin
from collections import deque

A, B = map(int, stdin.readline().split())
dq = deque()
dq.append((A,1))

while dq:
    
    num, count = dq.popleft()

    temp1 = int(str(num) + '1')
    temp2 = num * 2
    count += 1

    if temp1 == B:        
        print(count)
        break

    elif temp1 < B:
        dq.append((temp1, count))
    
    if temp2 == B:
        print(count)
        break

    elif temp2 < B:
        dq.append((temp2, count))

else:
    print(-1)

