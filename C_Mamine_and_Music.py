n, k = map(int, input().split())
arr = list(map(int, input().split()))

instruments = []

for i in range(n):
    instruments.append((arr[i], i + 1))

instruments.sort()

total_days = 0
chosen = []

for days, idx in instruments:
    if total_days + days <= k:
        total_days += days
        chosen.append(idx)
    else:
        break

print(len(chosen))
print(*chosen)