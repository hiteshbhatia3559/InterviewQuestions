# 5.18

# Write a program which takes an n x n 2D array and retums the spiral ordering of the array

import random

array_size = 4  # n x n
# a = [[random.randint(0, array_size) for _ in range(array_size)] for _ in range(array_size)]
a = [[_ for _ in range(4)] for _ in range(4)]
for item in a:
    print(item)

# O(n^2) iterative
def spiral1(a):
    spiral_array = []
    top, bottom, left, right = 0, len(a[0])-1, 0, len(a[0])-1
    direction = 0
    # 0 is right
    # 1 is down
    # 2 is left
    # 3 is up
    while top <= bottom and left <= right:
        if direction == 0:
            for i in range(left, right+1):
                spiral_array.append(a[top][i])
            top += 1
            direction = 1
        if direction == 1:
            for j in range(top, bottom+1):
                spiral_array.append(a[j][right])
            right -= 1
            direction = 2
        if direction == 2:
            for k in reversed(range(left, right+1)):
                spiral_array.append(a[bottom][k])
            bottom -= 1
            direction = 3
        if direction == 3:
            for l in reversed(range(top, bottom+1)):
                spiral_array.append(a[bottom][l])
            left += 1
            direction = 0
    return spiral_array


print(spiral1(a))
