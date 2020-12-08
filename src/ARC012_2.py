# import sys
# l = list(sys.stdin.readline().split())

n, takahashi_v, kame_v, kame = map(int, input().split())
takahashi = 0

for i in range(n):
    takahashi_time = kame / takahashi_v
    takahashi = kame
    kame = takahashi_time * kame_v

print(kame)
