
s = input()

for i in range(len(s)-2, 1, -2):
    harf = i // 2
    if s[0:harf] == s[harf:i]:
        print(i)
        exit()
