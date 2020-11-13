
m = 10 ** 9 + 7

n = int(input())
l = list(map(int, input().split()))

s = sum(l)
ans = 0

for i in l:
    s -= i
    ans += s * i

print(ans % m)
