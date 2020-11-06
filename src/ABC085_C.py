n, y = map(int, input().split())

def solve(n, y):
    for i in range(n+1):
        for j in range(n+1-i):
            if (i*1000 + j*5000 + (n-i-j)*10000 == y):
                return [(n-i-j), j, i]

ans = solve(n, y)

if ans is None:
    print("-1 -1 -1")
else:
    print(" ".join(map(str, ans)))
