s = input().split('-')
a = []
for i in s:
    a.append(i.split('+'))

res = 0

for i in range(len(a)):
    sum_ = 0
    for j in a[i]:
        sum_ += int(j)
    if i == 0:
        res = sum_
    else:
        res -= sum_
    if len(a) == 1: # 입력에 '-' 가 없을 때
        break

print(res)
