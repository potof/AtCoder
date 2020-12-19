
n = int(input())
x = list(map(int, input().split()))

m1 = sum(x) // len(x)
m2 = m1 + 1
a1 = [(i - m1)**2 for i in x]
a2 = [(i - m2)**2 for i in x]

print(min(sum(a1), sum(a2)))
