#!/usr/bin/env python2
# https://leetcode.com/problems/reverse-integer


class Solution(object):

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MAX_INT32 = 2**31 - 1
        MIN_INT32 = -2**31

        ans = 0
        isNegative = False
        if x != abs(x):
            x = abs(x)
            isNegative = True

        while x > 0:
            ans = ans * 10 + (x % 10)
            x = x / 10

        if isNegative:
            ans = -ans

        if ans > MAX_INT32 or ans < MIN_INT32:
            return 0

        return ans


def printTest(x, ans):
    out = Solution().reverse(x)

    if ans == out:
        print("Test passed for {0}: output {1} == {2}".format(x, out, ans))
    else:
        print("Test failed for {0}: output {1} <> {2}".format(x, out, ans))


if __name__ == '__main__':
    printTest(1, 1)
    printTest(10, 1)
    printTest(123, 321)
    printTest(-123, -321)
    printTest(-12345678999, 0)
