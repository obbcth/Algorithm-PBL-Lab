# 교차로

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
car = []
q = [deque() for _ in range(4)]

for _ in range(n):
    i = input().split()
    num = int(i[0]) # 차가 들어오는 시간
    pos = i[1] # 차가 들어오는 pos
    car.append([_, num, pos])

answer = [-1] * n
car.append([n, 2*10**9+1, 'A'])
counter = 0
idx = 0

while counter <= 2*10**9:

    c = car[idx]
    carnum, num, pos = c

    while num <= counter:
        if pos == "A":
            q[0].append(c)
        if pos == "B":
            q[1].append(c)
        if pos == "C":
            q[2].append(c)
        if pos == "D":
            q[3].append(c)
        idx += 1

        c = car[idx]
        carnum, num, pos = c

    # 교차로에 차가 쌓여있으면 -1
    if q[0] and q[1] and q[2] and q[3]:
        break

    # 차가 없으면 skip
    if not q[0] and not q[1] and not q[2] and not q[3]:
        counter = num
        continue

    for i in range(4):
        if q[i] and not q[(i-1) % 4]: # 오른쪽에 위치한 차가 없으면 통과
            x = q[i].popleft()
            number = x[0]
            answer[number] = counter

            if q[(i+2) % 4] and not q[(i+1) % 4]: # 맞은편 동시에 나갈 수 있으면
                x = q[(i+2) % 4].popleft()
                number = x[0]
                answer[number] = counter
            break
    
    counter +=1

for i in range(n):
    print(answer[i])
