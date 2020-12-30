
n = int(input())
rate_list = list(map(int, input().split()))

rate_flg = [False for _ in range(8)]
upper_count = 0

for rate in rate_list:
    if 1 <= rate <= 399:
        rate_flg[0] = True
    elif 400 <= rate <= 799:
        rate_flg[1] = True
    elif 800 <= rate <= 1199:
        rate_flg[2] = True
    elif 1200 <= rate <= 1599:
        rate_flg[3] = True
    elif 1600 <= rate <= 1999:
        rate_flg[4] = True
    elif 2000 <= rate <= 2399:
        rate_flg[5] = True
    elif 2400 <= rate <= 2799:
        rate_flg[6] = True
    elif 2800 <= rate <= 3199:
        rate_flg[7] = True
    elif 3200 <= rate:
        upper_count += 1

min_color = 1 if sum(rate_flg) == 0 else sum(rate_flg)
max_color = sum(rate_flg) + upper_count

print(min_color, max_color)
