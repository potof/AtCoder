
n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

x = [i[0] for i in xy]
xc = [x.count(i) for i in x]
y = [i[1] for i in xy]
yc = [y.count(i) for i in y]
if max(xc) >= 3 or max(yc) >= 3:
    print("Yes")
else:
    k = [i[1] - i[0] for i in xy]
    kc = [k.count(i) for i in k]
    if max(kc) >= 3:
        print("Yes")
    else:
        print("No")