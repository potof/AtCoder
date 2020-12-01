num = int(input())

def gcd(a, b):
    r = a % b
    return gcd(b, r) if r else b

ans = 0
for i in range(1, num+1):
    for j in range(1, num+1):
        for k in range(1, num+1):
            ans += gcd(i, gcd(j, k))

print(ans)