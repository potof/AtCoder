
n = input()
a_list = list(map(int, input().split()))

ans = 0
high = a_list[0]

for i in range(1, len(a_list)):
    if high >= a_list[i]:
        ans += high - a_list[i]
    else:
        high = a_list[i]

print(ans)
