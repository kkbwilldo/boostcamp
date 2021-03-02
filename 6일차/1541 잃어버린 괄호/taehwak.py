equ = list(input().split('-'))
cnt = sum(map(int, equ[0].split('+')))
for num in equ[1:]:
    cnt -= sum(map(int, num.split('+')))
print(cnt)