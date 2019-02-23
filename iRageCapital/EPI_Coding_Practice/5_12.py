# 5.12

# Implement an algorithm that takes as input an array of distinct elements and a size, and returns
# a subset of the given size of the array elements. All subsets should be equally likely. Return the
# result in input array itself.

import random

# O(k)
def select_subset(k, a):
    for i in range(k):
        r = random.randint(0, len(a) - 1)
        a[i], a[r] = a[r], a[i]
    return a[:3]

a = [1, 3, 5,7]
k = 3

print(select_subset(k, a))
