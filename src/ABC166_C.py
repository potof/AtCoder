
_, road_count = map(int, input().split())
high_list = list(map(int, input().split()))
road_list = [list(map(int, input().split())) for _ in range(road_count)]

ans = [0 for _ in range(len(high_list))]

for road in road_list:
    if high_list[road[0]-1] == high_list[road[1]-1]:
        ans[road[0]-1] += 1
        ans[road[1]-1] += 1
    elif high_list[road[0]-1] > high_list[road[1]-1]:
        ans[road[1]-1] += 1
    else:
        ans[road[0]-1] += 1

print(ans.count(0))



# ans = 0
# for i in high_list:
#     beauty_flg = True
#     for road in road_list:
#         if road[0] == i:
#             if high_list[road[0]-1] <= high_list[road[1]-1]:
#                 beauty_flg = False
#                 break
#         elif road[1] == i:
#             if high_list[road[0]-1] >= high_list[road[1]-1]:
#                 beauty_flg = False
#                 break
#     if beauty_flg:
#         ans += 1

# print(ans)
