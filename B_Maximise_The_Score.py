n = int(input())
for _ in range(n):
  t = int(input())
  arr = list(map(int, input().split()))
  arr.sort(reverse=True)
  ans = 0
  left = 0
  for right in range(1,len(arr),2):
    ans += min(arr[left], arr[right])
    left += 2
  print(ans)