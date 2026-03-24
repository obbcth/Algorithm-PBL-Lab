# 로드밸런서 트래픽 예측

from collections import deque

N, K = map(int, input().split())

tree = {}
count = {}

indegree = [0] * (N+1)

for i in range(N):
    g = list(map(int, input().split()))
    r = g[0]
    p = g[1:]

    tree[i+1] = p

    for t in p:
        indegree[t] += 1

que = deque([1])
count[1] = K

while len(que) != 0:
    cur = que.popleft()

    for idx, leaf in enumerate(tree[cur]):
        if leaf in count:
            count[leaf] += count[cur] // len(tree[cur])
        else:
            count[leaf] = count[cur] // len(tree[cur])

        if count[cur] % len(tree[cur]) - idx > 0:
            count[leaf] += 1

        indegree[leaf] -= 1
        if indegree[leaf] == 0:
            que.append(leaf)

for i in range(1, N+1):
    print(count.get(i, 0), end=" ")
