# def perm(arr, n):
#     res = []

#     if n > len(arr):
#         return res

#     if n == 1:
#         for i in arr:
#             res.append([i])
#     else:
        
#         for i in range(len(arr)):
#             temp = arr[:]
#             temp.remove(arr[i])

#             for t in perm(temp, n-1):
#                 res.append([arr[i]] + t)
#     return res

N = sorted(list(map(str,input())), reverse=True)
answer = -1

if sum([int(i) for i in N]) % 3 == 0 and N[-1] == '0':
    print("".join(N))
else:
    print(-1)
    