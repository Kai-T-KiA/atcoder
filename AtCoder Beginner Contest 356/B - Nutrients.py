N, M = map(int, input().split())

A = list(map(int, input().split()))

X = []

for i in range(N):
  x = list(map(int, input().split()))
  X.append(x)



for i in range(M):
  sum = A[i]
  for j in range(N):
    sum = sum - X[j][i]
  if sum > 0:
    print('No')
    exit()

print('Yes')

