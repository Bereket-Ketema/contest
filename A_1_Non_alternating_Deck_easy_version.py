n = int(input())
for i in range(n):
  k = int(input())
  a, b = 1, 0
  i = 2
  while a + b < k:
    if (a+b+i) > k:
      b += k - (a+b)
      break
    b += i
    i += 1
    if (a+b+i) > k:
      b += k - (a+b)
      break
    if a+b == k:
      break
    b += i
    i += 1
    if (a+b+i) > k:
      a += k - (a+b)
      break
    if a+b == k:
      break
    a += i
    i += 1
    if (a+b+i) > k:
      a += k - (a+b)
      break
    if a+b == k:
      break
    a += i
    i += 1
  print(a,b)
    