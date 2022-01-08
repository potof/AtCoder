
n = int(input())

l = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    x1 = l[i][0]
    y1 = l[i][1]
    for j in range(i+1, n):
        x2 = l[j][0]
        y2 = l[j][1]
        ans = max(ans, ((x2-x1)**2 + (y2-y1)**2)**0.5)

print(ans)