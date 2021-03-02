from sys import stdin
#stdin =  open("bj-study/input.txt","r")
n=int(stdin.readline())
nums=[]
for _ in range(n):
    nums.append(int(stdin.readline()))
nums.sort()

pivot=0
for i,num in enumerate(nums):
    if num > 0: # 음수랑 0을 같은 쪽으로 묶어서 최대한 제거해 주는것이 좋다.
        pivot=i
        break
left=nums[:i]
right=nums[i:]
right=right[::-1] #큰수 부터 정렬되도록
result=0
for i,num in enumerate(left): #left "-" numbers
    if i%2==0 and i!=len(left)-1: # 짝수 인덱스 and 끝 인덱스가 아님
        result+= num*left[i+1]
    if len(left)%2!=0 and i==len(left)-1:
        result+= num
# print(result)

for i,num in enumerate(right):
    if num==1: # 양수에서는 1끼리 곱해서 없어지면 손해기 때문에 최대한 살려야 한다.
        result+=num
    else: #1 아닐때는 두개씩 묶어서 큰순서대로 곱해줘야한다.
        if i%2==0 and i!=len(right)-1: # 짝수 인덱스 and 끝 인덱스가 아님
            result+= num*right[i+1]
        if len(right)%2!=0 and i==len(right)-1:
            result+= num
print(result)
