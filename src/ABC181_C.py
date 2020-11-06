
n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
print(xy)
x, y = [(a, b) for a, b in *xy]
print(x, y)
