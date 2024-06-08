A,B = map(int, input().split())

person = [1,2,3]

if A != B:
  person.remove(A)
  person.remove(B)
else:
  person.remove(A)



if (len(person) == 1):
  print(person[0])
else:
  print(-1)
