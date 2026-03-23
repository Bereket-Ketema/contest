n, k = map(int, input().split())
s = input()

freq = [0] * 26
for ch in s:
    freq[ord(ch) - ord('a')] += 1

result = []
last = -10

for i in range(26):
    if freq[i] > 0:
        if last == -10 or i >= last + 2:
            result.append(i)
            last = i
            if len(result) == k:
                break

if len(result) < k:
    print(-1)
else:
    total = sum(x + 1 for x in result)
    print(total)