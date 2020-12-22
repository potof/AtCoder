# TLE
#
# s = input()
# ans = 0
# while True:
#     s = s.replace("BW", "WB", 1)
#     ans += 1
#     if "BW" not in s:
#         break
# print(ans)

# AC !!
s = input()
ans = 0
location = 0

for i in range(len(s)):
    if s[i] == "W":
        ans += i - location
        location += 1

print(ans)