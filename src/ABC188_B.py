
# ----------------------------
# 愚直パターン
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# ans = 0
# for i in range(n):
#     ans += a[i] * b[i]

# 上記を省略したパターン
ans = sum(map(lambda a: a[0] * a[1], zip(a, b)))
ans = sum([a[i] * b[i] for i in range(n)])

if ans == 0:
    print("Yes")
else:
    print("No")


# ----------------------------
# numpy パターン（こっちのほうが遅い）
# import numpy as np

# n = int(input())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# ans = np.dot(a, b)

# if ans == 0:
#     print("Yes")
# else:
#     print("No")
