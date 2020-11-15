

sx, sy, gx, gy = map(int, input().split())

a = (-gy-sy) / (gx-sx)
b = sy - (sx * a)

print(-b/a)
