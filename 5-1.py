# 비밀 메뉴 2

n, m, k = map(int, input().split())

p = list(map(int, input().split()))
q = list(map(int, input().split()))

dp = [[0] * (m+1) for _ in range(n+1)]
answer = 0

for i in range(1, n+1):
    for j in range(1, m+1):
        if p[i-1] == q[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            answer = max(answer, dp[i][j])
        else:
            dp[i][j] = 0

print(answer)
