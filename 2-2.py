# 회의실 예약

N, M = map(int, input().split())

rooms = {}

for _ in range(N):
    name = input()
    rooms[name] = [0, 0, 0, 0, 0, 0, 0, 0, 0] # 9 ~ 18시

for _ in range(M):
    r, s, t = input().split()
    s = int(s)
    t = int(t)

    for i in range(s, t):
        rooms[r][i - 9] = 1

for i, room in enumerate(sorted(rooms.keys())):
    print(f'Room {room}:')

    period = []

    idx = 0
    while idx < 9:
        if rooms[room][idx] == 0:
            start = idx
            while idx < 9 and rooms[room][idx] == 0:
                idx += 1
            end = idx
            period.append((start, end))
        else:
            idx += 1
    
    if len(period) == 0:
        print('Not available')
    else:
        print(f'{len(period)} available:')
        for start, end in period:
            print(f'{start + 9:02d}-{end + 9:02d}')

    if i != len(rooms) - 1:
        print('-----')
