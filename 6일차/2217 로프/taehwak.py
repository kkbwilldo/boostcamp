n = int(input())
ropes = sorted([int(input()) for _ in range(n)], reverse=True)
max_weight = 0
for i in range(n):
    max_weight = max(ropes[i]*(i+1), max_weight)
print(max_weight)
