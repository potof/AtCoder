# dream dreamer erase eraser
s = input()

a = s.replace("eraser", "")
b = a.replace("erase", "")
c = b.replace("dreamer", "")
d = c.replace("dream", "")

if len(d) == 0:
    print("YES")
else:
    print("NO")
