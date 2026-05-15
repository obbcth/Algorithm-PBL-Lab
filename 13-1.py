# 자동차 테스트

n, q = map(int, input().split())

cars = list(map(int, input().split()))
cars = sorted(cars) # 정렬

# 연비 중앙값 계산 - 주어지는 자동차는 연비가 서로 다름을 가정해도 좋음
count = {cars[i]: i * (n-i-1) for i in range(n)}

for _ in range(q):
    t = int(input())
    print(count.get(t, 0))
