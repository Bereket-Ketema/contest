t = int(input())
for _ in range(t):
  n = input()
  r = "314159265358979323846264338327"
  count = 0
  for i in range(len(n)):
    if n[i] != r[i]:
      break
    count += 1
  print(count)