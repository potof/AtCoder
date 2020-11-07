import math
n = input()
x = tuple(map(int, input().split()))

print(sum(tuple(map(abs, x))))
print(math.sqrt(sum(tuple(map(lambda i:i**2, x)))))
# print(sum(tuple(map(lambda i:i**2, x))) ** 0.5)
print(max(tuple(map(abs, x))))
