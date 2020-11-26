
x, n = map(int, input().split())
p_list = list(map(int, input().split()))

for i in range(x+1):
    # マイナスからやらないとだめ（同じ場合は小さい方を回答するから）
    for j in [-1, 1]:
        ans = x + i*j
        if ans not in p_list:
            print(ans)
            exit()
