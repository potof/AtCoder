
n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))

ans_list = [abs(a - (t - (i * 0.006))) for i in h]

print(ans_list.index(min(ans_list)) + 1)
