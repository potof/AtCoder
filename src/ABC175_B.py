
n = input()
l = list(map(int, input().split()))

l.sort()

ans = 0
if len(l) < 3:
    print(ans)
    exit()

for i in range(len(l)-2):
    for j in range(i+1, len(l)-1):
        for k in range(i+2, len(l)):
            if l[i] < l[j] < l[k] and l[k] < l[i]+l[j]:
                # print(l[i], l[j], l[k])
                ans += 1

print(ans)
