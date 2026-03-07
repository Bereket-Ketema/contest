n, b = map(int, input().split())
a = list(map(int, input().split()))

costs = []
odds = 0
evens = 0

for i in range(n - 1):
    if a[i] % 2 == 0:
        evens += 1
    else:
        odds += 1
    
    if evens == odds:
        cost = abs(a[i] - a[i+1])
        costs.append(cost)
        
costs.sort()

total_cuts = 0
current_spent = 0

for c in costs:
    if current_spent + c <= b:
        current_spent += c
        total_cuts += 1
    else:
        break
        
print(total_cuts)