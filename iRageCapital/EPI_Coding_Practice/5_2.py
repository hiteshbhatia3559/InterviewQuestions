# 5.2
#
# Write a program which takes as input an array of digits encoding a nonnegative decimal integer
# D and updates the array to represent the integer D + 1. For example, if the input is (7,2,9) then
# you should update the array to (1,3,0). Your algorithm should work even if it is implemented in a
# language that has finite-precision arithmetic.


# Extended for adding any number with carry
def add_number(a, number):
    if a[-1] + number <= 9:
        a[-1] = a[-1] + number
    else:
        a[-1] = a[-1] + number
        if a[-1] == 10:
            carry = 1
        else:
            carry = a[-1] % 10
        a[-1] = a[-1] - 10
        a[:-1] = add_number(a[:-1], carry)

    return a

a = [1, 9, 8]
number = 1
print(add_number(a, number))

# Out of scope problems
# It cannot add numbers > 2 for some reason, not thinking because its outside the scope of the problem
