# 염기서열 커버

n, m = map(int, input().split())

# a c g t . (wildcard)
arr = []
for _ in range(n):
    l = input()
    arr.append(l)

# bitmask: arr의 index를 bit로 나열, 해당 bit를 단일로 나타낼 수 있는가 TF
good = []
for i in range(2**n):
    group = [arr[j] for j in range(n) if i & (1<<j)]
    
    compatible = True
    for j in range(m):
        agct = set()
        for g in group:
            if g[j] != '.':
                agct.add(g[j])
            if len(agct) > 1:
                compatible = False
                break

    # arr에 대해서 하나의 염기서열로 충족하는가 tf
    good.append(compatible)

dp = [n] * (2**n)
dp[0] = 0

for i in range(1, 2**n):

    # s의 부분집합 순회, good이면 dp i 갱신
    s = i
    while s > 0:
        if good[s]:
            dp[i] = min(dp[i], dp[i^s] + 1)
        s = (s-1) & i

print(dp[2**n-1])
