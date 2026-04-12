# 로봇이 지나간 경로

h, w = map(int, input().split())

m_list = []

for _ in range(h):
    m = input()
    m_list.append(m)

point = []

def around_sharp(x, y):
    count = 0
    if x-1 >= 0 and m_list[x-1][y] == "#":
        count += 1
    if x+1 < h and m_list[x+1][y] == "#":
        count += 1
    if y-1 >= 0 and m_list[x][y-1] == "#":
        count += 1
    if y+1 < w and m_list[x][y+1] == "#":
        count += 1
    return count

def where_to_go(x, y):
    print(x+1, y+1)
    if x-1 >= 0 and m_list[x-1][y] == "#":
        return "^"
    if x+1 < h and m_list[x+1][y] == "#":
        return "v"
    if y-1 >= 0 and m_list[x][y-1] == "#":
        return "<"
    if y+1 < w and m_list[x][y+1] == "#":
        return ">"

def how_to_go(x, y, d, end_x, end_y):
    print("A", end="")

    if d == "^":
        x -= 2
    if d == "v":
        x += 2
    if d == "<":
        y -= 2
    if d == ">":
        y += 2

    if x == end_x and y == end_y:
        return
    
    if x-1 >= 0 and m_list[x-1][y] == "#":
        if d == "^":
            how_to_go(x, y, d, end_x, end_y)
        elif d == "<":
            print("R", end="")
            how_to_go(x, y, "^", end_x, end_y)
        elif d == ">":
            print("L", end="")
            how_to_go(x, y, "^", end_x, end_y)

    if x+1 < h and m_list[x+1][y] == "#":
        if d == "v":
            how_to_go(x, y, d, end_x, end_y)
        elif d == "<":
            print("L", end="")
            how_to_go(x, y, "v", end_x, end_y)
        elif d == ">":
            print("R", end="")
            how_to_go(x, y, "v", end_x, end_y)

    if y-1 >= 0 and m_list[x][y-1] == "#":
        if d == "<":
            how_to_go(x, y, d, end_x, end_y)
        elif d == "^":
            print("L", end="")
            how_to_go(x, y, "<", end_x, end_y)
        elif d == "v":
            print("R", end="")
            how_to_go(x, y, "<", end_x, end_y)

    if y+1 < w and m_list[x][y+1] == "#":
        if d == ">":
            how_to_go(x, y, d, end_x, end_y)
        elif d == "^":
            print("R", end="")
            how_to_go(x, y, ">", end_x, end_y)
        elif d == "v":
            print("L", end="")
            how_to_go(x, y, ">", end_x, end_y)

for i in range(h):
    for j in range(w):
        if m_list[i][j] == "#":
            if around_sharp(i, j) == 1:
                point.append((i, j))

direction = where_to_go(*point[1])
print(direction)

how_to_go(*point[1], direction, *point[0])
