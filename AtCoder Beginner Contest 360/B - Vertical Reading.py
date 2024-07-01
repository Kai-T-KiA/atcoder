# 問題URL https://atcoder.jp/contests/abc360/tasks/abc360_b

S, T = input().split()

w = 1

while w < len(S):
  listS = [list(S[i: i+w]) for i in range(0, len(S), w)]
  for i in range(w):
    comb = []
    for s in listS:
      if len(s) >= i+1:
        comb.append(s[i])
    
    if T == ''.join(comb):
      print('Yes')
      exit()
  w += 1

print('No')
