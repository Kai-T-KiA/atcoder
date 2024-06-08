# 問題URL https://atcoder.jp/contests/abc355/tasks/abc355_b

N, M = map(int, input().split())

A = list(map(int, input().split()))

B = list(map(int, input().split()))

A.sort()

B.sort()

countA = 0
countB = 0

before = 'C'
after = 'C'

sortList = []

while countA <= len(A) - 1 and countB <= len(B) - 1:
  # for i in range(len(A+B)):
  if countA == len(A) - 1:
    countB += 1
    before = after
    after = 'B'
  elif countB == len(B) - 1:
    countA += 1
    before = after
    after = 'A'
  elif A[countA] < B[countB]:
    countA += 1
    before = after
    after = 'A'
  else:
    countB += 1
    before = after
    after = 'B'

  if before == 'A' and after == 'A':
    print('Yes')
    exit()

print('No')
