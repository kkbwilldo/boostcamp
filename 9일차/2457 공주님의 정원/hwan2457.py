from sys import stdin

N = int(stdin.readline())

day_31 = [3,5,7,8,10,12]
day_30 = [4,6,9,11]
day_dictionary = [0,31,59]

for i in range(3, 13):
    if i in day_31:
        day_dictionary.append(day_dictionary[i-1] + 31)
    else:
        day_dictionary.append(day_dictionary[i-1] + 30)


flower = [list(map(int, stdin.readline().split())) for _ in range(N)]

arr = []
for j in range(len(flower)):
    start_date = day_dictionary[flower[j][0] - 1] + flower[j][1]
    end_date = day_dictionary[flower[j][2] - 1] + flower[j][3]
    arr.append((start_date, end_date))

arr.sort(key=lambda x:(x[0], x[1]))

answer = []
i = day_dictionary[2]
idx = -1
changed = False
chk = 0

while i <= 334 and idx < N:
    changed = False
    idx += 1

    for k in range(idx, N):
        
        if arr[k][0] > i:
            break
        if chk < flower[k][1]:
            chk = flower[k][1]
            idx = k
            changed = True
    
    if changed:
        i = chk
        answer.append(arr[idx])
    else:
        answer = []
        break

print(len(answer))
