from collections import Counter

s = input()

# 2 桁以下のとき
if len(s) <= 2:
    if (int(s) % 8 == 0) or (int(s[::-1]) % 8  == 0):
        print("Yes")
    else:
        print("No")
    exit()

c = Counter(s)
# 3 桁以上のとき
# 8 で割り切る場合は下3桁で判断できる
for i in range(104, 1000, 8):
    ic = Counter(str(i))
    if not ic - c:
        print("Yes")
        exit()
print("No")


# TLE 愚直に順列を回すと TLE だった
# import itertools
# for i in itertools.permutations(s):
#     if int("".join(i)) % 8 == 0:
#         print("Yes")
#         exit()
# print("No")
