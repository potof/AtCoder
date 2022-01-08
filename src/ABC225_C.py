
import numpy as np


n, m = map(int, input().split())


b = np.array([list(map(int, input().split())) for _ in range(n)])
ans_list = np.array([[b[0][0] + (7 * i)+ j for j in range(m)] for i in range(n)])

if np.array_equal(b, ans_list):
    print("Yes")
else:
    print("No")
