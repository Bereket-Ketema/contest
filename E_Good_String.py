n = int(input())
s = input()

res = []

for char in s:
    if len(res) % 2 == 0:
        res.append(char)
    else:
        if res[-1] != char:
            res.append(char)

if len(res) % 2 == 1:
    res.pop()

print(n - len(res))
print("".join(res))