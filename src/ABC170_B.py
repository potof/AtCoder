# import sys
# l = list(sys.stdin.readline().split())

x, y = map(int, input().split())

kame = 4
turu = 2

for i in range(x + 1):
    if kame*i + turu*(x-i) == y:
        print("Yes")
        exit()
print("No")