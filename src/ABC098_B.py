
n = int(input())
s = list(input())

ans_list = [0 for _ in range(n)]

for sep in range(n-1):
    search_word = s[sep]

    for i in range(0, sep+1):
        if s[i] in s[sep+1:] and s[0:i+1].count(s[i]) == 1:
            ans_list[sep] += 1

print(max(ans_list))
