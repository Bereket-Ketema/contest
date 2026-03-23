def check(n, m):
  if n == m:
    return True
  if n % 3 != 0:
    return False
  
  return check(n // 3, m) or check(2 * n // 3, m)

for _ in range(int(input())):
  n, m = map(int, input().split())
  print("YES" if check(n, m) else "NO")