n = int(input())
for _ in range(n):
  a,b = map(int,input().split())
  store = list(map(int,input().split()))
  store1 = set(store)
  count = 0
  i = 0
  while count < b:
    if i not in store1:
      store1.add(i)
      count += i
    if count > b:
      break
    i += 1
  if count > b:
    print("NO")
  else:
    for i in range(1,max(store1)+1):
      if i in store1:
        if i == max(store1):
          print("YES")
        else:
          continue
      else:
        print("NO")
        break  