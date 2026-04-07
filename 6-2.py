# 트럭
import bisect

n = int(input())
events = {}

for i in range(n):
    nums = list(map(int, input().split()))
    weights = nums[1::2]
    vals = nums[2::2]
    for w, v in zip(weights, vals):
        if w not in events:
            events[w] = []
        events[w].append((i, v))

best_val = [0] * n
temp = 0

sorted_ws = sorted(events.keys())

answer = []
answer_threshold = []

for w in sorted_ws:
    for i, v in events[w]:
        if v > best_val[i]:
            temp += v - best_val[i]
            best_val[i] = v
    answer.append(w)
    answer_threshold.append(temp)

m = int(input())
q_list = list(map(int, input().split()))

for q in q_list:
    index = bisect.bisect_left(answer_threshold, q)

    if index == len(answer_threshold):
        print(-1, end=" ")
    else:
        print(answer[index], end=" ")
