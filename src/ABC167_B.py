
a, b, c, k = map(int, input().split())

ans = 0

if a <= k:
    ans = a
else:
    ans = k
k -= a

if k > 0:
    k -= b

if k > 0:
    ans -= k

print(ans)