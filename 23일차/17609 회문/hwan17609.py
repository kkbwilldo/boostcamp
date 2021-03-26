from sys import stdin

T = int(stdin.readline())

answer = []

for i in range(T):

    input_ = stdin.readline().rstrip()
    if input_ == input_[::-1]:
        # print(input_, input_[::-1])
        print(0)
    else:
        point_a = 0
        point_b = len(input_) - 1

        while point_a <= point_b:

            # print(point_a,point_b, input_[point_a], input_[point_b])
            if input_[point_a] == input_[point_b]:
                point_a += 1
                point_b -= 1
            else:
                if input_[point_a+1:point_b+1] == input_[point_a+1:point_b+1][::-1]:
                    print(1)
                    break
                elif input_[point_a:point_b] == input_[point_a:point_b][::-1]:
                    print(1)
                    break
                else:
                    print(2)
                    break
            
