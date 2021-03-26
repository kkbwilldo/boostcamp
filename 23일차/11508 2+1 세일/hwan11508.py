from sys import stdin

N = int(stdin.readline())

num_arr = sorted([int(stdin.readline()) for _ in range(N)],reverse=True)
answer = 0

for i in range(0,N,3):

    answer += sum(num_arr[i:i+3])
    # print(num_arr[i:i+3])
    if len(num_arr[i:i+3]) == 3:
        # print(answer)
        answer -= min(num_arr[i:i+3])
        # print(min(num_arr[i:i+3]), answer)

print(answer)