# 좌석 관리

N, M, Q = map(int, input().split())

progress = [0] * 10001 # 0: doesn't eat, 1: eats, 2: finished
seat = {}
seat_map = [[0] * M for _ in range(N)]

def get_seat(id):
    if len(seat.keys()) == 0:
        seat[id] = (1, 1)
        seat_map[0][0] = id
        return (1, 1)

    priority = 0
    candidates = []
    
    for i in range(N):
        for j in range(M):
            if seat_map[i][j] != 0:
                continue
            if j-1 >= 0 and seat_map[i][j-1] != 0:
                continue
            if j+1 < M and seat_map[i][j+1] != 0:
                continue
            if i-1 >= 0 and seat_map[i-1][j] != 0:
                continue
            if i+1 < N and seat_map[i+1][j] != 0:
                continue

            fartest_priority = 9999999999
            for seated_id in seat.keys():

                x, y = seat[seated_id]
                dist = pow(x - (i + 1), 2) + pow(y - (j + 1), 2)

                if dist < fartest_priority:
                    fartest_priority = dist
            
            if fartest_priority > priority:
                priority = fartest_priority
                candidates = [(i + 1, j + 1)]
            
            elif fartest_priority == priority:
                candidates.append((i + 1, j + 1))

    if candidates:
        result = sorted(candidates, key=lambda x: (x[0], x[1]))[0]
        seat[id] = result
        seat_map[result[0] - 1][result[1] - 1] = id
        return result
    
    return -1

for _ in range(Q):
    in_out, id = input().split()

    id = int(id)
    
    if in_out == 'In':
        if progress[id] == 1:
            print(str(id) + " already seated.")
            continue
        if progress[id] == 2:
            print(str(id) + " already ate lunch.")
            continue

        result = get_seat(id)
        if result == -1:
            print("There are no more seats.")
        
        else:
            print(str(id) + " gets the seat " + str(result) + ".")
            progress[id] = 1

    if in_out == 'Out':
        if progress[id] == 0:
            print(str(id) + " didn't eat lunch.")
            continue

        if progress[id] == 2:
            print(str(id) + " already left seat.")
            continue

        print(str(id) + " leaves from the seat " + str(seat[id]) + ".")
        progress[id] = 2
        seat_map[seat[id][0] - 1][seat[id][1] - 1] = 0
        del seat[id]
