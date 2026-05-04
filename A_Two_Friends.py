t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    
    p = [x - 1 for x in p]
    
    found_two_cycle = False
    for i in range(n):
        if p[p[i]] == i:
            found_two_cycle = True
            break
    
    if found_two_cycle:
        print(2)
    else:
        print(3)