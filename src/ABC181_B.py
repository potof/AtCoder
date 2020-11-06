
n = int(input())

ans = 0

# 等差数列の和 を使う
# 初項a、公差d、項数n
def tousasuuretu_no_wa(a, d, n):
    return n/2 * (2*a + (n-1) * d)

for _ in range(n):
    a, n = map(int, input().split())
    ans += tousasuuretu_no_wa(a, 1, n-a+1)

print(int(ans))

# 遅い
# l = [list(map(int, input().split())) for _ in range(n)]
# ans = [sum(range(a[0], a[1]+1)) for a in l]
# print(sum(ans))

# 遅い
# ans = 0
# for _ in range(n):
#     a, b = map(int, input().split())
#     ans += sum(range(a, b+1))
# print(ans)
