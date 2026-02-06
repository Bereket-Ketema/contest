n, m = map(int,input().split())
arr = [int(num) for num in input().split()]
count = 0
for i in range(n):
  if arr[i] > 0 and arr[i] >= arr[m-1]:
    count +=1
print(count)