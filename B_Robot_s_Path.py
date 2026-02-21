n, k = map(int,input().split())
obstacle = input()
left = 1
while left < n:
  for j in range(left, left + k):
    if obstacle[j] != "#":
      left = j + 1
      break
    if j == left + k - 1:
      print("NO")
      exit()
print("YES")