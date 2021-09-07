n = int(input())
l = list(map(int, input().split()))

ans = [0 for _ in range(n)]

for i in range(n):
    ans[l[i]-1] = i + 1

print(*ans)
