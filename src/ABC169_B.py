
n = int(input())
nums = list(map(int, input().split()))

if 0 in nums:
    print(0)
    exit()

nums.sort(reverse=True)
ans = 1
for i in nums:
    ans *= i
    if ans > pow(10, 18):
        ans = -1
        break

print(ans)
