from sys import stdin

N = int(stdin.readline())

num_arr = [int(stdin.readline()) for _ in range(N)]
answer = 0
for i in range(N-1,0,-1):
    if num_arr[i-1] >= num_arr[i]:
        answer += num_arr[i-1] - (num_arr[i] - 1)
        num_arr[i-1] = num_arr[i] - 1
print(answer)