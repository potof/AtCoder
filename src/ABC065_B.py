
n = int(input())
button = [int(input()) for _ in range(n)]
button.insert(0, -1)
using_flg = [0 for _ in range (n+1)]

current_button = 1
using_flg[current_button] = 1

ans = 0

for i in range(n):
    current_button = button[current_button]
    ans += 1

    if current_button == 2:
        print(ans)
        exit()

    if using_flg[current_button] == 1:
        print(-1)
        exit()
    using_flg[current_button] = 1
