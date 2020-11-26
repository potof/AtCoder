
x, n = map(int, input().split())
p_list = list(map(int, input().split()))

a1 = 101
b1 = 101

for i in range(x-1, -1, -1):
    if i not in p_list:
        a1 = i
        break

for i in range(x, 101):
    if i not in p_list:
        b1 = i
        break

if abs(x-a1) > abs(x-b1):
    print(b1)
else:
    print(a1)
