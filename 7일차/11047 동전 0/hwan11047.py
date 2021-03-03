N, K = map(int, input().split())
num_arr = sorted([int(input()) for _ in range(N)], reverse=True)
answer = 0
for i in num_arr:
    if K >= i:
        answer += K // i
        K = K % i
print(answer)