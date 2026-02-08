n = int(input())

arr = [int(num) for num in input().split()]

def check(arr,value):
  count = 0
  for i in arr:
    if i > value:
      count += 1
  return count

for i in range(n):
  print(check(arr,arr[i]) + 1,end=" ")