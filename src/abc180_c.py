
n = int(input())

def divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

l = divisors(n)
print(*l, sep="\n")

# 愚直にやったら TLE だった
# for i in range(1, n+1):
#     if n % i ==0:
#         print(i)
