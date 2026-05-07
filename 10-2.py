# 통근버스 출발 순서 검증하기

n = int(input())
l = list(map(int, input().split()))

answer = 0

for i in range(n):
    d = [0] * (n+1)
    for j in range(i):
        if l[i] > l[j]:
            d[l[j]] = 1
    for j in range(n-1, 0, -1):
        d[j] += d[j+1]
    for j in range(i+1, n):
        answer += d[l[j]]

print(answer)
