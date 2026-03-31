# 거리 합 구하기

import sys
sys.setrecursionlimit(100000)

n = int(input())
m = [[] for _ in range(n+1)]
dist = [0] * (n+1)
size = [0] * (n+1)

for _ in range(n-1):
    x, y, t = map(int, input().split())

    m[x].append((y, t))
    m[y].append((x, t))

def dfs(num, parent, cur):
    dist[num] = cur
    size[num] = 1

    for i, t in m[num]:
        if i != parent:
            dfs(i, num, cur + t)
            size[num] += size[i]

visited = [0] * (n+1)
dfs(1, -1, 0)

ans = [0] * (n+1)
ans[1] = sum(dist)

def reroot(num, parent):
    for i, t in m[num]:
        if i != parent:
            ans[i] = ans[num] - size[i]*t + (n-size[i])*t
            reroot(i, num)

reroot(1, 1)

for i in ans[1:]:
    print(i)
