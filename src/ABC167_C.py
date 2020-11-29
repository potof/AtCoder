# import sys
# l = list(sys.stdin.readline().split())
import itertools

n, m, goal = map(int, input().split())

books = [list(map(int, input().split())) for _ in range(n)]

ans = []

for i in range(1, n+1):
    for books_combi in itertools.combinations(books, i):
        ability_sum = list(map(sum, zip(*books_combi)))
        # print(ability_sum)

        goal_flg = True
        for j in ability_sum[1:m+1]:
            if j < goal:
                goal_flg = False

        if goal_flg:
            ans.append(ability_sum[0])

if ans:
    print(min(ans))
else:
    print(-1)
