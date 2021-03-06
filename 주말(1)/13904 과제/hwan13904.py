from sys import stdin

N = int(stdin.readline())


assignment = sorted([list(map(int, stdin.readline().split())) for _ in range(N)],
                    key=lambda x:(x[0],x[1]), reverse=True)

answer = []
last_date = assignment[0][0]

for day in range(last_date, 0, -1):
    temp = -1
    idx = 0

    for j in range(N):

        if day > assignment[j][0]:
            break

        if day <= assignment[j][0] and temp < assignment[j][1]:
            temp = assignment[j][1]
            idx = j

    if temp != -1:
        answer.append(temp)
        assignment[idx][1] = -1

print(sum(answer))