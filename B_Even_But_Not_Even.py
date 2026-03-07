t = int(input())
def check(m):
  if (m[-1]) % 2 != 0:
    return True
  return False
def check2(m):
  if sum(m) % 2 == 0:
    return True
  return False

for _ in range(t):
  n = int(input())
  num = list(map(int, input()))

  if check(num) and check2(num):
    print(''.join(map(str, num)))
    continue

  if n == 1:
    print(-1)
    continue

  while len(num) > 0 and not check(num):
      num.pop(-1)
  
 
  flag = False
  while len(num) > 1:
    if not check2(num):
      num.pop(-2)
    else:
      print(''.join(map(str, num)))
      flag = True
      break

  if not flag:
    print(-1)