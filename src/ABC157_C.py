
n, m = map(int, input().split())

zyouken = [list(map(int, input().split())) for _ in range(m)]

for i in range(1000):
    ans = str(i)
    if len(ans) != n:
        continue

    ans_flg = True
    for keta, value in zyouken:
        if int(ans[keta-1]) != value:
            ans_flg = False
            break

    if ans_flg:
        print(i)
        exit()

print(-1)
