# 問題URL https://atcoder.jp/contests/abc363/tasks/abc363_b

N, T, P = map(int, input().split())

L = list(map(int, input().split()))

day = 0

while True:
  count = 0

  for l in L:
    if l >= T:
      count += 1

  if count >= P:
    print(day)
    exit()
  else:
    day += 1

  for i in range(N):
    L[i] = L[i] + 1
