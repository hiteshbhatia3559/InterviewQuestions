# 5.`17
#
# Check whether a 9 x9 2D array representing a partially completed Sudoku is valid. Specifically,
# check that no row, column, or 3 x 3 2D subarray contains duplicates. A O-value in the 2D array
# indicates that entry is blank; every other entry is in [1,9].

# Defining constraints for myself here...
# 1. any row or column in the 9x9 array cannot have repetitions
# 2. each block 3x3 in the 9x9 array is definite, non-overlapping and cannot have repetitions in itself
# 3. We need 5 sets of valid sudoku puzzles to verify this works (and we'll make a randomize function that generates
# a random sudoku puzzle)

