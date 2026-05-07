# 업무 처리

from collections import deque

h, k, r = map(int, input().split())
k_list = [deque() for _ in range(2**(h+1)-1)]
inputs = []  # 말단 직원의 원본 업무 리스트

# 완전이진트리
for i in range(2**h):
    inputs.append(deque(map(int, input().split())))

answer = 0
for day in range(1, r+1):
    for employee in range(2**h-1):
        if k_list[employee*2 + 1 + (day+1)%2]:
            e = k_list[employee*2 + 1 + (day+1)%2].popleft()
            if employee == 0:
                answer += e
            else:
                k_list[employee].append(e)

    # 말단 직원이 그날 1개씩 올림
    for i in range(2**h):
        if inputs[i]:
            k_list[2**h - 1 + i].append(inputs[i].popleft())

print(answer)
