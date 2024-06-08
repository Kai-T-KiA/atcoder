S = input()

upperCount = 0
lowerCount = 0

for s in S:
  judge = s.isupper()
  if judge == True:
    upperCount += 1
  else :
    lowerCount += 1

if upperCount > lowerCount:
  print(S.upper())
else:
  print(S.lower())
