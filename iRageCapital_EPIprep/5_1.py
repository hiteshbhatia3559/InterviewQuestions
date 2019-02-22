# 5.1

# Write a program that takes an array A and an index i into A, and rearranges the elements such
# that all elements less than A[r] (the "pivot") appear first, followed by elements equal to the pivot,
# followed by elements greater than the pivot.


def rearrange(a, i):
    a_left, a_right, a_middle = [], [], []
    for item in a:
        if item < a[i]:
            a_left.append(item)
        if item == a[i]:
            a_middle.append(item)
        if item > a[i]:
            a_right.append(item)
    return a_left + a_middle + a_right


a = [1, 5, 6, 7, 3, 2, 4, 6, 9, 1, 3, 4, 5]
i = 4
print(rearrange(a, i))
