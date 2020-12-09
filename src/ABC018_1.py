# AC using rankdata

# import numpy as np
# from scipy.stats import rankdata
# abc = rankdata(-np.array(([int(input()) for _ in range(3)])))
# [print(int(i)) for i in abc]


# AC not using rankdata
# こっちのほうが早い
abc = list([int(input()) for _ in range(3)])
sorted_abc = sorted(abc, reverse=True)

for i in abc:
    print(sorted_abc.index(i) + 1)
