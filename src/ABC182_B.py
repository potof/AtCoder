
n = int(input())
l = list(map(int, input().split()))

ans = []
for i in range(2, 1000 + 1):
    a = 0
    for j in l:
        if j < 2:
            continue
        elif j % i == 0:
            a += 1
    ans.append(a)

print(ans.index(max(ans)) + 2)
