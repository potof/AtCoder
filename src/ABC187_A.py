
a, b = input().split()

sum_a = sum([int(s) for s in a])
sum_b = sum([int(s) for s in b])

print(max(sum_a, sum_b))
