
n = int(input())

t = n
ans = ""

while t > 0:
    if t % 2 == 0:
        ans = "B" + ans
        t = t // 2
    else:
        ans = "A" + ans
        t = t - 1

print(ans)
