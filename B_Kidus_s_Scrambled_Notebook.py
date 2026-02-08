n = int(input())

for i in range(n):
  right = input()
  left = ""
  left += right[0]
  right = right[1:]
  for j in range(len(right)):
    if int(right) <= int(left):
      print(-1)
      break
    elif int(right[0]) != 0 and int(right) > int(left):
      print(left,right)
      break
    left += str(right[0])
    right = str(right[1:])