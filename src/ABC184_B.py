
n, x = map(int, input().split())
s = input()

ans = x
for result in s:
    if result == "o":
        ans += 1
    elif ans != 0:
        ans -= 1

print(ans)