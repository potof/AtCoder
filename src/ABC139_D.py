
# TLE
# n = int(input())
# ans = sum(list([i for i in range(1, n)]))
# print(ans)


# 左に一つずらして割っていくと、ni のあまりがでる
n = int(input())

# 公式 (n+1)xn/2
# 一つ左にずらした数字を n にする
rs = n-1
print((rs+1) * rs // 2)
