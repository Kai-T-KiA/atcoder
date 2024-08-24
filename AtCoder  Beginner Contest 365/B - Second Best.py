# 問題URL https://atcoder.jp/contests/abc365/tasks/abc365_b

N = int(input())

A = list(map(int, input().split()))

first = -1
first_num = -1
second = -1
second_num = -1

for i in range(N):
  if first == -1:
    first = A[i]
    first_num = i
  elif A[i] < first and second == -1:
    second = A[i]
    second_num = i
  elif A[i] > first:
    second = first
    second_num = first_num
    first = A[i]
    first_num = i
  elif A[i] < first and A[i] > second:
    second = A[i]
    second_num = i
  else:
    continue

print(second_num + 1)
