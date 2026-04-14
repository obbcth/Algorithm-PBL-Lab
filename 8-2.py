# Garage Game

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(3*n)]

answer = 0
dd = ((1,0),(-1,0),(0,1),(0,-1))

def anipang(board, x, y, seen):
    color = board[x][y]
    cells = [(x, y)]
    seen[x][y] = True
    mnr = mxr = x
    mnc = mxc = y

    q = deque([(x, y)])
    while q:
        r, c = q.popleft()
        for dr, dc in dd:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and not seen[nr][nc] and board[nr][nc] == color:
                seen[nr][nc] = True
                cells.append((nr, nc))
                if nr < mnr: mnr = nr
                elif nr > mxr: mxr = nr
                if nc < mnc: mnc = nc
                elif nc > mxc: mxc = nc
                q.append((nr, nc))

    score = len(cells) + (mxr - mnr + 1) * (mxc - mnc + 1)
    return cells, score

def slot_flush(slot, cells):
    # 열별로 제거할 '슬롯 절대 행' 모으기
    by_col = {}
    for r, c in cells:
        by_col.setdefault(c, set()).add(2*n + r)

    new_slot = [row[:] for row in slot]
    for c, rm in by_col.items():
        surv = [slot[r][c] for r in range(3*n) if r not in rm]
        offset = 3*n - len(surv)
        for i, v in enumerate(surv):
            new_slot[offset + i][c] = v
    return new_slot

def do(slot, rnd, point):
    global answer
    board = slot[-n:]

    # 보드의 모든 컴포넌트 수집
    seen = [[False]*n for _ in range(n)]
    groups = []  # list of (cells, score)
    for i in range(n):
        for j in range(n):
            if seen[i][j]:
                continue
            cells, score = anipang(board, i, j, seen)
            groups.append((cells, score))

    if rnd == 2:
        best = max(score for _, score in groups)
        if point + best > answer:
            answer = point + best
        return

    # 가지치기용 정렬
    groups.sort(key=lambda g: -g[1])

    # 상한 가지치기
    upper_per_round = 2 * n * n  # 한 라운드 최대 점수 상한
    if point + upper_per_round * (3 - rnd) <= answer:
        return

    for cells, score in groups:
        if point + score + upper_per_round * (3 - rnd - 1) <= answer:
            continue
        do(slot_flush(slot, cells), rnd + 1, point + score)

do(s, 0, 0)
print(answer)
