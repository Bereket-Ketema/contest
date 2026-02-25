n, size = map(int, input().split())
store = []

for _ in range(n):
    a, b = map(int, input().split())
    store.append((a, b))


total = sum(a for a, b in store)

store.sort(key=lambda x: (x[0] - x[1]), reverse=True)

count = 0

for a, b in store:
    if total <= size:
        print(count)
        exit()
    
    total -= (a - b)
    count += 1

if total <= size:
    print(count)
else:
    print(-1)