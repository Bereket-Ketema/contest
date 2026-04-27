import sys
sys.setrecursionlimit(10**7)

n = int(input())
cost = list(map(int, input().split()))

m = int(input())
adj = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)

# Tarjan's variables
disc = [-1] * n
low = [-1] * n
in_stack = [False] * n
stack = []
time = 0

MOD = 10**9 + 7
total_cost = 0
ways = 1

def dfs(u):
    global time, total_cost, ways
    
    disc[u] = low[u] = time
    time += 1
    stack.append(u)
    in_stack[u] = True
    
    for v in adj[u]:
        if disc[v] == -1:
            dfs(v)
            low[u] = min(low[u], low[v])
        elif in_stack[v]:
            low[u] = min(low[u], disc[v])
    
    # root of SCC
    if disc[u] == low[u]:
        scc = []
        while True:
            node = stack.pop()
            in_stack[node] = False
            scc.append(node)
            if node == u:
                break
        
        # process this SCC
        mn = min(cost[x] for x in scc)
        cnt = sum(1 for x in scc if cost[x] == mn)
        
        total_cost += mn
        ways = (ways * cnt) % MOD

for i in range(n):
    if disc[i] == -1:
        dfs(i)

print(total_cost, ways)