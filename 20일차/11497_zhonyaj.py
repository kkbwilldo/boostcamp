from sys import stdin
stdin = open("input.txt","r")
test_case = int(stdin.readline())
for t in range(test_case):
    m = int(stdin.readline())
    List = list(map(int,stdin.readline().split()))
    List.sort()
    temp = List[0::2]
    temp2 = List[1::2]
    temp+=temp2[::-1]
    Max=0
    for i in range(m):
        if i==m-1:
             Max = max(abs(temp[-1]-temp[0]),Max)
             continue
        Max = max(abs(temp[i]-temp[i+1]),Max)
    print(Max)
    