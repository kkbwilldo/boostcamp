from itertools import accumulate
n = int(input())
times = sum(accumulate(sorted(map(int, input().split()))))

print(times)