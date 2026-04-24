from collections import defaultdict

n, k = map(int, input().split())
sequence = list(map(int, input().split()))

def solve(n, k, sequence):
    freq = defaultdict(int)

    for x in sequence:
        freq[x] += 1

    for cnt in freq.values():
        if cnt > k:
            return []

    indexed = []
    for pos, val in enumerate(sequence):
        indexed.append([val, pos])

    indexed.sort()

    label = 1
    for val, pos in indexed:
        sequence[pos] = label
        label += 1
        if label > k:
            label = 1

    return sequence

answer = solve(n, k, sequence)

if answer:
    print("YES")
    print(*answer)
else:
    print("NO")