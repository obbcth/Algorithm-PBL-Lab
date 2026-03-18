# 마이크로서버

t = int(input())

for _ in range(t):
    __ = input()
    apps = sorted(list(map(int, input().split())))

    start = 0
    end = len(apps) - 1
    count = 0

    while start <= end and apps[end] > 600:
        count += 1
        end -= 1
    
    while start < end and apps[start] == 300 and apps[end] == 600:
        count += 1
        start += 1
        end -= 1
    
    app300 = 0
    while start <= end and apps[start] == 300:
        app300 += 1
        start += 1

    while start < end:
        if apps[start] + apps[end] <= 900:
            count += 1
            start += 1
            end -= 1
        elif app300 > 0:
            count += 1
            app300 -= 1
            end -= 1
        else:
            count += 1
            end -= 1

    if start == end:
        count += 1
        if app300 > 0:
            app300 -= 1

    print(count + (app300+2)//3)
