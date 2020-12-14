
# 1, 5, 3, 5    -4
# 8, 4, 4, 4    4
# 8, 12, 12, 3  -4
# 24, 20, 20, 2 4
# 40, 44, 44, 1 -4

a, b, c, k = map(int, input().split())

if abs(a-b) > 10**18:
    print("Unfair")
elif k % 2 == 1:
    print(-(a-b))
else:
    print(a-b)
