# import sys
# l = list(sys.stdin.readline().split())

k, n = map(int, input().split())
locations:list = list(map(int, input().split()))

distance = [0 for _ in range(n)]

for i in range(n):
    if i == n-1:
        distance[i] = (k - locations[i]) + locations[0]
    else:
        distance[i] = locations[i+1] - locations[i]

print(sum(distance) - max(distance))
