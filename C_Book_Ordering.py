n = int(input())
store = []
for i in range(n):
  r = list(map(int,input().split()))
  store.append(r)
max_ = max(store[0])
for i in range(1,n):
  if max_ < store[i][0] and max_ < store[i][1]:
    print("NO")
    exit()
  if store[i][0] <= max_ and store[i][1] <= max_:
    max_ = max(store[i])
  else:
    if store[i][0] <= max_:
      max_ = store[i][0]
    else:
      max_ = store[i][1]
 
print("YES")
