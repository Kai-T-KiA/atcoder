# 問題URL https://atcoder.jp/contests/abc357/tasks/abc357_a

N, M = map(int, input().split())

H = list(map(int, input().split()))

count = 0

for i in range(N):
  if N == 1:
    if M >= H[i]:
      print(1)
    else:
      print(0)
    exit()


  
  M -= H[i]

  if M >= 0:
    count += 1
  else:
    break

print(count)
