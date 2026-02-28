n = int(input())
for i in range(n):
  arr = input()
  if len(set(arr[:len(arr)//2])) > 1:
    print("YES")
  else:
    print("NO")