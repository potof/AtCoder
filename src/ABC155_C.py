
import collections

n = int(input())
words = [input() for _ in range(n)]

counter = collections.Counter(words)
max_num = max(counter.values())

ans = []
for value, count in counter.items():
    if count == max_num:
        ans.append(value)

ans.sort()
[print(s) for s in ans]
