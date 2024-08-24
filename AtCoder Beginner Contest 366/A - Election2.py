# 問題URL https://atcoder.jp/contests/abc366/tasks/abc366_a

N, T, A = map(int, input().split())

if T > N/2 or A > N/2:
  print('Yes')
else:
  print('No')
