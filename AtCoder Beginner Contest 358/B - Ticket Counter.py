N, A = map(int, input().split())

T = list(map(int, input().split()))

count = 0

for i in range(N):
  if i == 0:
    count = T[i] + A
    print(count)
  else:
    if T[i] < count:
      count += A
      print(count)
    else:
      count = count + (T[i] - count) + A
      print(count)