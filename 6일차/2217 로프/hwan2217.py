from sys import stdin

N = int(stdin.readline())

num_arr = [int(stdin.readline()) for _ in range(N)]
num_arr.sort(reverse=True)

answer = num_arr[0]

for i in range(1, len(num_arr)):
    answer = max(answer, num_arr[i] * (i+1))
    
print(answer)