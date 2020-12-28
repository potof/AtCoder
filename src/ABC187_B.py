import itertools

n = int(input())

points = [list(map(int, input().split())) for _ in range(n)]
combi_points = itertools.combinations(points, 2)

ans = 0

for l in combi_points:
    x = l[1][0] - l[0][0]
    y = l[1][1] - l[0][1]

    yx = y / x
    if 1 >= yx >= -1:
        ans += 1


print(ans)
