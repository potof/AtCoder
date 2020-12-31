
n, x = map(int, input().split())

drank_al = 0
for i in range(n):
    ml, al = map(int, input().split())

    drank_al += ml * al
    if drank_al > x * 100:
        print(i+1)
        exit()

print(-1)
