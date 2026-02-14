n = int(input())
for _ in range(n):
  t = int(input())
  word = input()
  right = ""
  if t == 1:
    print("NO")
    continue
  for i in range(1,t):
    right = word[i+1:]
    check = word[i-1] + word[i]
    if check  in right:
      print("YES")
      break
    if i == t-1:
      print("NO")