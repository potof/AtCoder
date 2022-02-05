


N = int(input())
A = list(map(int, input().split()))
aa = [0 for _ in range(N+1)]

cur = 0
is360 = False
for i in range(N):

    cur = cur + A[i]
    if cur > 360:
        t = cur - 360
        aa[i+1] = t
        cur = t
        is360 = True

    else:
        aa[i+1] = cur


# 90, 270, 315, 150
# 90, 60, 120,

aa.sort()
# print(aa)


ans = 0
if not is360:
    ans = 360 - sum(aa)

for i in range(len(aa)-1):
    left = aa[i]
    right = aa[i+1]

    if ans < right - left:
        ans = right - left

print(ans)
