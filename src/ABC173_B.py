import collections

n = int(input())
l = [input() for _ in range(n)]
c = collections.Counter(l)

print("AC", " x", c["AC"])
print("WA", " x", c["WA"])
print("TLE", " x", c["TLE"])
print("RE", " x", c["RE"])
