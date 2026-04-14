# 사물인식 최소 면적 산출 프로그램

n, K = map(int, input().split())
# 1부터 k까지 색은 하나 이상 있어야 됨

dots = []
area = 999999999

for _ in range(n):
    x, y, k = map(int, input().split())
    dots.append([x, y, k])

xs = sorted(set(d[0] for d in dots))

for x1 in xs:
    for x2 in xs:
        if x2 < x1: continue
        filtered = [dot for dot in dots if x1 <= dot[0] <= x2]
        ys = sorted(set(d[1] for d in filtered))
        for y1 in ys:
            for y2 in ys:
                if y2 < y1: continue
                visited = [0] * (K+1)
                for dot in filtered:
                    if y1 <= dot[1] <= y2:
                        visited[dot[2]] = 1
                if sum(visited) == K:
                    area = min(area, (x2-x1)*(y2-y1))

print(area)
