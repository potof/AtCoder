import copy

n = input()
if sum(list(map(int, n))) % 3 == 0:
    print(0)
    exit()

ans = -1
for i in range(len(n)):
    for j in range(1, len(n)):
        t = sum(list(map(int, n[:i] + n[i+j:len(n)-i])))
        if t % 3 == 0 and not t == 0:
            print(j)
            exit()
print(ans)
