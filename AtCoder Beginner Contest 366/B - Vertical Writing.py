# 問題URL https://atcoder.jp/contests/abc366/tasks/abc366_b

N = int(input())

S = [list(input()) for _ in range(N)]

S_output = []

max_len = -1

for s in S:
  if len(s) > max_len:
    max_len = len(s)


for i in range(max_len):
  info = ''
  for j in range(N):
    if len(S[N-1-j]) != 0:
      chr = S[N-1-j].pop(0)
    else:
      chr = '*'
    info += chr

  S_output.append(info)

for s in S_output:
  if '*' not in s:
    print(s)
  else:
    if s[-1] != '*':
      print(s)
    else:
      while True:
        if s[-1] == '*':
          s = s[:-1]
        else:
          print(s)
          break
