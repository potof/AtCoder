import math

n, d = map(int, input().split())

ans = 0

for i in range(n):
    x, y = map(int, input().split())
    if math.sqrt(x**2 + y**2) <= d:
        ans += 1

print(ans)
