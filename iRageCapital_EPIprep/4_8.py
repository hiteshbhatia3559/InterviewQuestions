# 4.8
#
# Write a program which takes an integer and returns the integer corresponding to the digits of the
# input written in reverse order. For example, the reverse of 42is 24, and the reverse of -314 is -413.

#Accepts all input

def revString(s):
    try:
        if int(s) < 0:
            return -abs(int(s))
        else:
            return s[::-1]
    except:
        return s[::-1]


print(revString("-12"))