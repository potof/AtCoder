
a, b = map(int, input().split())
c, d = map(int, input().split())

if a==c and b==d:
    print(0)

elif a+b == c+d or a-b == c-d or abs(a-c) + abs(b-d) <= 3:
    print(1)

elif (a+b) % 2 == 0 and (c+d) % 2 == 0:

    print(2)

elif (a+b) % 2 == 0 and (c+d) % 2 == 1:
    if abs(c)-3 + abs(a)+3 <= 6 or abs(d)-3 + abs(b)+3 <=6:
        print(2)
    else:
        print(3)
else:
    print(3)