# 강의 문제

import sys
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())

# s -> t / t -> s 모두 만족시켜야 하기 때문
edge = [[] for _ in range(n+1)]
edgeR = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    edge[x].append(y)
    edgeR[y].append(x)

s, t = map(int, input().split())

visited_sx = [0] * (n+1) # 출발지에서 도달가능한 노드 s -> x
visited_tx = [0] * (n+1) # 도착지에서 도달가능한 노드 t -> x
visited_xs = [0] * (n+1) # 출발지로 갈 수 있는 노드 x -> s
visited_xt = [0] * (n+1) # 도착지로 갈 수 있는 노드 x -> t

def dfs(cur, adj, visit):
    if visit[cur] == 1:
        return
    
    visit[cur] = 1
    for nxt in adj[cur]:
        dfs(nxt, adj, visit)
    return

# 도착지에 도달하면 끝
visited_sx[t] = 1
visited_tx[s] = 1

dfs(s, edge, visited_sx)
dfs(t, edge, visited_tx)

dfs(s, edgeR, visited_xs)
dfs(t, edgeR, visited_xt)

count = 0
for i in range(n+1):
    if visited_sx[i] and visited_tx[i] and visited_xs[i] and visited_xt[i]:
        count += 1

# 출도착 빼기
print(count-2)
