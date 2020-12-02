
# 偶数, 偶数 and n > k
# 100, 80 = 100/80 1 amari 20
# 100, 50 = 100/50 2 amari 0

# 奇数, 偶数 and n > k
# 11, 4 = 11/4 2 amari 3  ans = -1
# 15, 8 = 15/8 1 amari 7  ans = -1
# 5, 2 = 5/2 2 amari 1 ans = 1 or -1

# 偶数, 奇数
# 10, 3 = 10/3 3 amari 1 ans = 1

# 奇数, 奇数
# 9, 5 = 9/5 1 amari 4 ans = -1
# 11, 5 = 11/5 2 amari 1 ans = 1 not -4

n, k = map(int, input().split())

amari = n%k

if abs(amari - k) > amari:
    print(amari)
else:
    print(abs(amari - k))
