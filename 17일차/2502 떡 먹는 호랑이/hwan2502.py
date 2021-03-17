from sys import stdin

D, K = map(int, stdin.readline().split())

def chk_num(a_count, b_count):
    for i in range(1,K):
        for j in range(1, K):
            
            if i * a_count + j * b_count == K:
                return i, j
            if i * a_count + j * b_count > K:
                break

a, b = 'a', 'b'

dp = [''] * (D+1)
dp[1] = a
dp[2] = b

for i in range(3,D+1):
    dp[i] = dp[i-2] + dp[i-1]

a_count, b_count = dp[-1].count('a'), dp[-1].count('b')

answer_a, answer_b = chk_num(a_count, b_count)
print(answer_a)
print(answer_b)