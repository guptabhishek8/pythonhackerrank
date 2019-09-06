import numpy as np
x,y = map(int, input().split())
my_array= np.array([input().split() for _ in range(x)], int)
print(np.transpose(my_array))
print(my_array.flatten())


