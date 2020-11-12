
n = int(input())

count = 0

for a in range(1, n):
    for b in range(a, n):
        if n - a*b > 0:
            if a == b:
                count += 1
            else:
                count += 2
        else:
            break

print(count)
