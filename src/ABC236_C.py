
N, M = map(int, input().split())
S = list(input().split())
M = set(input().split())

for station in S:
    if station in M:
        print("Yes")
    else:
        print("No")
