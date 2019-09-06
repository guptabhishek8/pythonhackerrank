import numpy
arr = list(map(int , input().split(" ")))
changed_arr = numpy.array(arr)
changed_arr.shape = (3,3)
print(changed_arr)



