
h,w = map(int, input().split())

rows = []
for i in range(h):
    rows += list(map(int, input().split()))

min_num = min(rows)

ans = sum(list(map(lambda i: i - min_num, rows)))
print(ans)
