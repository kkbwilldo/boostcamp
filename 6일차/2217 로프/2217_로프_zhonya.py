from sys import stdin
stdin = open("bj-study/input.txt","r")
n=int(stdin.readline())
temp=[]
for _ in range(n):
    temp.append(int(stdin.readline()))

def sol(input_list):
    max_v=0
    length=len(input_list)
    for i,t in enumerate(sorted(input_list)):
        max_temp = t*(length-i) # i번 부터 n번까지 값을 모두 사용 할때의 값
        if max_v<max_temp: #새로운값이 더 크면 최대값 갱신, 처음엔 종료조건을 생각했는데 그냥 다 돌려도 된다.
            max_v=max_temp
    return max_v
print(sol(temp))