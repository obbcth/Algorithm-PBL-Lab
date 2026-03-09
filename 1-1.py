# 비밀 메뉴

m, n, k = list(map(int, input().split()))

M = input().split()
N = input().split()

secret = False
for i in range(n):
    if M == N[i : i + m]:
        secret = True
        break

if secret:
    print("secret")
else:
    print("normal")
