n = int(input())
store = list(map(int,input().split()))
s = set(store)
for i in range(1,n+1):
  if i not in s:
    print(i)