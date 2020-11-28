# import sys
# l = list(sys.stdin.readline().split())

n, k = map(int, input().split())
l = list(map(int, input().split()))
l.sort()

print(sum(l[:k]))
