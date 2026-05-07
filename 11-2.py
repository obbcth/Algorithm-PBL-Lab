# 성적 평가

import sys
input = sys.stdin.readline

n = int(input())
s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))
s3 = list(map(int, input().split()))
total = [s1[i] + s2[i] + s3[i] for i in range(n)]

def get_ranks(arr):
    rank_map = {}
    for i, score in enumerate(sorted(arr, reverse=True)):
        if score not in rank_map:
            rank_map[score] = i + 1
    return [rank_map[s] for s in arr]

print(" ".join(map(str, get_ranks(s1))))
print(" ".join(map(str, get_ranks(s2))))
print(" ".join(map(str, get_ranks(s3))))
print(" ".join(map(str, get_ranks(total))))
