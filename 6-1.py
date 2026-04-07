# 코딩 테스트 세트

n, t = map(int, input().split())

def possible(k):
    left = 0
    for i in range(n):
        available = s[2*i] + left
        right = s[2*i+1]

        if available >= k:
            left = right

        else:
            need = k - available
            if right >= need:
                left = right - need
            else:
                return False

    return True

for _ in range(t):
    s = list(map(int, input().split())) + [0]

    low, high = 0, sum(s)
    while low < high:
        mid = (low + high + 1) // 2
        if possible(mid):
            low = mid
        else:
            high = mid - 1

    print(low)
