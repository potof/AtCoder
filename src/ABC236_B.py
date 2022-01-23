import collections

n = int(input())

l = list(map(int, input().split()))
c = collections.Counter(l)

print(c.most_common()[-1][0])