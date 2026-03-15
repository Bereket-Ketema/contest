import sys

input = sys.stdin.read
data = input().split()

index = 0
t = int(data[index])
index += 1

results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    
    s = [int(data[index + i]) for i in range(n)]
    index += n
    
    if n == 1:
        results.append("-1")
        continue
    
    p = list(range(1, n+1))
    
    can_shift = all(s[i] <= s[(i+1) % n] for i in range(n))
    
    if can_shift:
        results.append(' '.join(map(str, p[1:] + p[:1])))
        continue
    
    perm = list(range(n))
    
    i = 0
    while i < n-1:
        if s[i] == s[i+1]:
            perm[i], perm[i+1] = perm[i+1], perm[i]
            i += 2
        else:
            i += 1
    
    is_derangement = all(perm[i] != i for i in range(n))
    is_valid = all(s[i] <= s[perm[i]] for i in range(n))
    
    if is_derangement and is_valid:
        ans = [perm[i] + 1 for i in range(n)]
        results.append(' '.join(map(str, ans)))
    else:
        results.append("-1")

print('\n'.join(results))