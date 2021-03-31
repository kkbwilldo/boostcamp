from sys import stdin

N, M = map(int, stdin.readline().split())

num_arr = list(map(int,stdin.readline().split()))

start = max(num_arr)
end = sum(num_arr)

answer = 0
while start <= end:
    middle = (start + end) // 2
    # print(start, middle, end)
    chk = 0
    count = 0
    for i in range(len(num_arr)):

        if chk + num_arr[i] > middle:
            count += 1
            chk = num_arr[i]
        else:
            chk += num_arr[i]
    count += 1

    if count == M:
        answer = middle
        end = middle - 1
    elif count < M:
        end = middle - 1
    # if count <= M:
    #     answer = middle
    #     end = middle - 1

    else:
        start = middle + 1

print(answer)