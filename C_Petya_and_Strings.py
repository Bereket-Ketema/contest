n = input()
m = input()
n = n.lower()
m = m.lower()
for i in range(len(n)):
  if n[i] < m[i]:
    print(-1)
    exit()
  if n[i] > m[i]:
    print(1)
    exit()
print(0)