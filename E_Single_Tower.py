import sys

input = sys.stdin.read
data = input().split()

index = 0
n = int(data[index])
index += 1

towers = []
all_vals = []

for i in range(n):
    k = int(data[index])
    index += 1
    tower = []
    for j in range(k):
        val = int(data[index])
        tower.append(val)
        all_vals.append(val)
        index += 1
    towers.append(tower)


sorted_vals = sorted(all_vals)
rank = {sorted_vals[i]: i + 1 for i in range(len(sorted_vals))}


total_runs = 0
for tower in towers:
    if not tower:
        continue
    rlist = [rank[val] for val in tower]
    runs = 1
    for j in range(1, len(rlist)):
        if rlist[j] != rlist[j - 1] + 1:
            runs += 1
    total_runs += runs

s = total_runs - n
c = total_runs - 1
print(s, c)