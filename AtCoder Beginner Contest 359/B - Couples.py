# 問題URL https://atcoder.jp/contests/abc359/tasks/abc359_b

N = int(input())

S = [input() for _ in range(N)]

count = 0

for s in S:
  if s == 'Takahashi':
    count += 1

print(count)
