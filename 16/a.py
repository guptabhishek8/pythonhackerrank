import numpy as np
n , m = map(int, input().split())
my_arr = np.array([input().split() for _ in range(n)], dtype = int)
print(np.prod(np.sum(my_arr, axis=0), axis =0))
