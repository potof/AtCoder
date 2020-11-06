n = int(input())

ans = True
current = [0, 0, 0]
for i in range(n):
    m, x, y = map(int, input().split())

    xy = abs(current[1] - x) + abs(current[2] - y)
    md = m - current[0]
    if not md == xy:
        if not ((md > xy) and ((md % 2 == 0) or (md % 3 == 0))):
            ans = False
            break
    current = [m, x, y]

if ans:
    print("Yes")
else:
    print("No")