t = int(input())
for _ in range(t):
  n = int(input())
  enemy = list(map(int, input()))
  dawit = list(map(int, input()))

  count = 0
  flag = True
  for i in range(n):
    if dawit[i] == 1:
      if i - 1 >= 0 and enemy[i - 1] == 1:
        count += 1
        enemy[i - 1] += 1
        flag = False
      
      if flag and enemy[i] == 0:
        count += 1
        enemy[i] = 2
        flag = False

      if flag and i + 1 < n and enemy[i + 1] == 1:
        enemy[i + 1] += 1
        count += 1
      
    flag = True

  print(count)