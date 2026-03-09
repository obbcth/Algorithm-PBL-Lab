# 전광판

marker = {
    "-": [0, 0, 0, 0, 0, 0, 0],
    "0": [1, 1, 1, 0, 1, 1, 1],
    "1": [0, 0, 1, 0, 0, 1, 0],
    "2": [1, 0, 1, 1, 1, 0, 1],
    "3": [1, 0, 1, 1, 0, 1, 1],
    "4": [0, 1, 1, 1, 0, 1, 0],
    "5": [1, 1, 0, 1, 0, 1, 1],
    "6": [1, 1, 0, 1, 1, 1, 1],
    "7": [1, 1, 1, 0, 0, 1, 0],
    "8": [1, 1, 1, 1, 1, 1, 1],
    "9": [1, 1, 1, 1, 0, 1, 1],
}

test_cases = int(input())

for _ in range(test_cases):
    count = 0
    a, b = input().split()
    a = a.rjust(5, '-')
    b = b.rjust(5, '-')

    for i in range(5):
        for j in range(7):
            if marker[a[i]][j] != marker[b[i]][j]:
                count += 1

    print(count)
