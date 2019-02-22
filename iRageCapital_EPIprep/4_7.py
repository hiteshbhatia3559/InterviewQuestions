# 4.7

# Write a program that takes a double x and an integer y and retums x/. You can ignore overflow and
# underflow.

import time

#O(n)
def power1(x,y):
    result = 1
    a = 0
    while (a < y):
        result *= x
        a += 1
    return result


print(power1(500,500))

#O(2^n)
def power2(x,y):
    if y == 0:
        return 1
    if y>=1:
        return x * power2(x,y-1)

