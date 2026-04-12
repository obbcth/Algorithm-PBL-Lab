# 안전운전을 도와줄 차세대 지능형 교통시스템

import sys
from collections import deque
input = sys.stdin.readline

n, T = map(int, input().split())
lights = [[list(map(int, input().split())) for _ in range(n)] for _ in range(n)]

signals = [
    None,
    (3, [1,1,0,1]),
    (0, [1,0,1,1]),
    (2, [1,1,1,0]),
    (1, [0,1,1,1]),
    (3, [1,0,0,1]),
    (0, [1,0,1,0]),
    (2, [0,1,1,0]),
    (1, [0,1,0,1]),
    (3, [0,1,0,1]),
    (0, [1,0,0,1]),
    (2, [1,0,1,0]),
    (1, [0,1,1,0]),
]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False]*n for _ in range(n)]
visited[0][0] = True
count = 1

q = deque([(0, 0, 0)]) # init cond 0,0 위쪽 방향

time = 0
while q and time < T:
    for _ in range(len(q)):
        x, y, d = q.popleft()
        sig = lights[x][y][time % 4]
        req_dir, allowed = signals[sig]

        if d != req_dir: # 교차로 진입방향 안맞으면 continue
            continue

        for nd in range(4):
            if allowed[nd]:
                nx, ny = x + dx[nd], y + dy[nd]
                if 0 <= nx < n and 0 <= ny < n:
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        count += 1
                    q.append((nx, ny, nd))
    time += 1

print(count)
