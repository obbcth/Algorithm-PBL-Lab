# 순서대로 방문하기

n, m = map(int, input().split())
tbl = []
for _ in range(n):
    t = list(map(int, input().split()))
    tbl.append(t)

todo = []

for _ in range(m):
    t = list(map(int, input().split()))
    todo.append([t[0] - 1, t[1] - 1])

# 시작점
start = todo[0]

# 좌표는 항상 unique하게 주어진다 가정
# 한번 지나간덴 다시 못지나감 = visited

answer = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visit = [[0] * n for _ in range(n)]

def dfs(x, y, idx):
    global answer
    
    if [x, y] == todo[idx]:
        if idx == m-1:
            answer += 1
            return
        
        idx += 1

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0 and tbl[nx][ny] == 0:
            visit[nx][ny] = 1
            dfs(nx, ny, idx)
            visit[nx][ny] = 0

visit[start[0]][start[1]] = 1
dfs(start[0], start[1], 1)

print(answer)
