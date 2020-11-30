import collections

n = int(input())
zyousi = collections.Counter(list(map(int, input().split())))

for i in range(1, n+1):
    print(zyousi[i])