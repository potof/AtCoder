
a, b = map(int, input().split())

# a, b が最大 100 なので、最大値は x * 0.1 = 100
for i in range(1001):
    if a == int(i*0.08) and b == int(i*0.1):
        print(i)
        exit()

# 存在しなかった場合
print(-1)