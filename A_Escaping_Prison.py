t = int(input())
for _ in range(t):
  store = 0
  n, h = map(int, input().split())
  for i in range(n):
    a, b = map(int, input().split())
    store += max(a, b)
  if store >= h:
    print("YES")
  else:
    print("NO")