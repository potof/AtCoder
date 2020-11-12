
m = 1000000007

n = int(input())

print((pow(10, n, m) - pow(9, n, m) * 2 + pow(8, n, m)) % m)