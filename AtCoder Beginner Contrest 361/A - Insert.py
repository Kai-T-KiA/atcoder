# 問題URL https://atcoder.jp/contests/abc361/tasks/abc361_a

N, K, X = map(int, input().split())

A = list(map(int, input().split()))

A.insert(K, X)

for a in A:
  print(a, end=' ')

print()
