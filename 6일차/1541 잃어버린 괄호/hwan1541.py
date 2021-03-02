num_arr = input().split('-')
answer = sum(map(int, num_arr[0].split('+')))

for i in num_arr[1:]:    
    answer -= sum(map(int, i.split('+')))

print(answer)

