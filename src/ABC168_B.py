# import sys
# l = list(sys.stdin.readline().split())

# n, m = map(int, input().split())
# l = [input() for _ in range(n)]

k = int(input())
s = input()

if len(s) > k:
    print(s[0:k], "...", sep="")
else:
    print(s)
