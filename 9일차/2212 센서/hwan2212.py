from sys import stdin

N = int(stdin.readline())
K = int(stdin.readline())

input_ = set(map(int, stdin.readline().split()))

loc = sorted(input_)
distance = []

for i in range(1, len(loc)):
    distance.append(loc[i] - loc[i-1])

distance.sort()

count = 0

while count < K-1 and distance:
    distance.pop()
    count += 1

print(sum(distance))