
a, b, c, k = map(int, input().split())

ans = min(a, k)
k -= a

if k > 0:
    k -= b

if k > 0:
    ans -= k

print(ans)