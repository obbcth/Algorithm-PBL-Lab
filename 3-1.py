# 이미지 프로세싱
import sys
sys.setrecursionlimit(10**5)

h, w = map(int, input().split())

colors = []

def poison(x, y, color, saved):

    if colors[x][y] != color:
        colors[x][y] = color

        if x>0 and colors[x-1][y] == saved:
            poison(x-1, y, color, saved)
        
        if x<h-1 and colors[x+1][y] == saved:
            poison(x+1, y, color, saved)
        
        if y>0 and colors[x][y-1] == saved:
            poison(x, y-1, color, saved)
        
        if y<w-1 and colors[x][y+1] == saved:
            poison(x, y+1, color, saved)


for _ in range(h):
    color_list = list(map(int, input().split()))
    colors.append(color_list)

q = int(input())

for _ in range(q):
    i, j, c = map(int, input().split())

    if colors[i-1][j-1] != c:
        poison(i-1, j-1, c, colors[i-1][j-1])

for i in colors:
    print(" ".join(list(map(str,i))))
