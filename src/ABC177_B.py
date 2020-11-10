
s = input()
t = input()

ans = 100000000

for i in range(len(s) - len(t) + 1):

    score = len(t)
    diff = s[i:i+len(t)]
    for j in range(len(t)):
        if diff[j] == t[j]:
            score -= 1
    ans = min(ans, score)

print(ans)