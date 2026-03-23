def check(a, b, store):
  if a == b:
    return True
  if a > b:
    return False
  if b % 2 != 0 and b % 10 != 1:
    return False
  if b % 2 == 0:
    store.append(b // 2)
    return check(a, b // 2, store)
  else:
    store.append(b // 10)
    return check(a, b // 10, store)
a, b = map(int, input().split())
store = [b]
response = check(a, b, store)
if response:
  print("YES")
  print(len(store))
  print(*store[::-1])
else: print("NO")