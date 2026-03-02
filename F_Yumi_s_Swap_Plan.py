n = int(input())
s = input().strip()

totalH = s.count('H') # H: 3
s = s + s # circular -> hth + hth = hthhth

current = 0
for i in range(totalH):
    if s[i] == 'T':
        current += 1

answer = current
for i in range(1, n):
    # remove left character
    if s[i - 1] == 'T':
        current -= 1
    
    # add new right character
    if s[i + totalH - 1] == 'T':
        current += 1
    
    answer = min(answer, current)

print(answer)