t = int(input())

for _ in range(t):
  n, l, r = map(int, input().split())
  arr = list(map(int, input().split()))
  
  store = 0
  left,right = 0, 0
  ans = 0
  while right < n:
    store += arr[right]

    while store > r:
      store -= arr[left]
      left += 1

    if store >= l and store <= r:
      ans += 1
      store = 0
      left = right + 1
     
    right += 1
  print(ans)    