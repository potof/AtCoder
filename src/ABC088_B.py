
n = int(input())
l = list(map(int, input().split()))

l.sort(reverse=True)

alice = sum(l[0::2])
bob = sum(l[1::2])

print(alice - bob)
