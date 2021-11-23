
n = int(input())

l = [0 for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    l[a-1] += 1
    l[b-1] += 1

if max(l) == n-1:
    print("Yes")
else:
    print("No")
