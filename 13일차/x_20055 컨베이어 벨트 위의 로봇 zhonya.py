from sys import stdin
from collections import deque
stdin = open("input.txt","r")
n,k = map(int,stdin.readline().split())
belt = deque(map(int,stdin.readline().split()))
print(belt)
robot=deque([])
cnt=0
if __name__ in "__main__":
    for _ in range(40):
        cnt+=1
        print(cnt)
        #1.회전
        belt.appendleft(belt.pop())
        for i in range(len(robot)):
            robot[i]+=1
            if robot[i]>=2*n-1:
                robot[i]=-1
        #2.벨트위 로봇 이동
        if robot:
            for i in range(len(robot)-1):
                if robot[i]>=2*n-1:
                    robot[i]=-1
                if belt[robot[i]+1]!=0 and belt.count(robot[i])<2:
                    robot[i]+=1
                    belt[robot[i]]-=1
                if robot[i]==n-1:
                    robot.popleft()
        print(belt)
        print(robot)
        #3.로봇 탑승
        robot.append(0)
        belt[0]-=1
        print(belt)
        print(robot)
        #4.내구도 0 k개 종료
        if belt.count(0)==k:
            print(cnt)
            break