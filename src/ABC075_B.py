

h, w = map(int, input().split())
maps = [list(input()) for _ in range(h)]


for i in range(h):
    for j in range(w):
        if maps[i][j] == ".":

            rows = ""
            if i != 0:
                if j != 0:
                    rows += maps[i-1][j-1]
                if j != w-1:
                    rows += maps[i-1][j+1]
                rows += maps[i-1][j]

            if j != 0:
                rows += maps[i][j-1]

            if j != w-1:
                rows += maps[i][j+1]

            if i != h-1:
                if j != 0:
                    rows += maps[i+1][j-1]
                if j != w-1:
                    rows += maps[i+1][j+1]
                rows += maps[i+1][j]
            maps[i][j] = str(rows.count("#"))


for m in maps:
    print("".join(m))
