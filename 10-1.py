# 슈퍼컴퓨터 클러스터

import sys, math
input = sys.stdin.readline

n, b = map(int, input().split())
power = list(map(int, input().split()))

def cost(x):
    total = 0
    for p in power:
        if p < x:
            total += (x - p) * (x - p)
            if total > b:   # 조기 종료 (큰 값에서 오버플로/속도 방지)
                return total
    return total

lo = min(power)
hi = lo + math.isqrt(b) + 1

while lo < hi:
    mid = (lo + hi + 1) // 2
    if cost(mid) <= b:
        lo = mid
    else:
        hi = mid - 1

print(lo)