l = [input() for _ in range(3)]
contests = ("ABC", "ARC", "AGC", "AHC")

for c in contests:
    if not c in l:
        print(c)
