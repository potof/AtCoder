
n = int(input())

ans = len(set([tuple((input().split())[1:]) for _ in range(n)]))

print(ans)
