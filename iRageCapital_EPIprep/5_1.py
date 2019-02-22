# 5.1

# Write a program that takes an array A and an index i into A, and rearranges the elements such
# that all elements less than A[r] (the "pivot") appear first, followed by elements equal to the pivot,
# followed by elements greater than the pivot.

# O(n) additional space complexity, O(n) time complexity


def rearrange1(a, i):
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
print(rearrange1(a, i))


# output = [1, 2, 1, 3, 3, 5, 6, 7, 4, 6, 9, 4, 5]

# O(1) additional space complexity, O(n) time complexity


def rearrange2(a, i):
    pivot = a[i]
    smaller = 0
    for item in range(len(a)):
        if a[item] < pivot:
            a[item], a[smaller] = a[smaller], a[item]
            smaller += 1
    larger = len(a) - 1
    for item in reversed(range(len(a))):
        if a[item] < pivot:
            break
        elif a[item] > pivot:
            a[item], a[larger] = a[larger], a[item]
            larger -= 1
    return a


print(rearrange2(a, i))

