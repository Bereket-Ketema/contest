n = int(input())
arr = list(map(int, input().split()))
if max(arr) > 25:
  print(max(arr) - 25)
else:
  print(0)