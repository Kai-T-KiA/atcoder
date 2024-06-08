N, L, R = map(int, input().split())

A = [i+1 for i in range(N)]

B = A[L-1:R]

B.sort(reverse=True)

newList = A[:L-1] + B + A[R:]

for i in newList:
  print(i, end=' ')


