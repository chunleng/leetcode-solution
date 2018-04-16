#!/usr/bin/env python2
# https://leetcode.com/problems/palindrome-number


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x < 0):
            return False

        if (x < 10):
            return True

        if (x % 10 == 0):
            return False

        x = abs(x)

        reverted = 0

        while (reverted < x):
            tail = x % 10
            reverted = reverted * 10 + tail
            x = x / 10

            if (reverted == x or reverted == x / 10):
                return True

        return False


def printTest(x, ans):
    out = Solution().isPalindrome(x)

    if ans == out:
        print("Test passed for {0}: output {1} == {2}".format(x, out, ans))
    else:
        print("Test failed for {0}: output {1} <> {2}".format(x, out, ans))


if __name__ == '__main__':
    s = Solution()

    printTest(0, True)  # single digit
    printTest(1, True)  # single digit
    printTest(-1, False)  # negative
    printTest(10, False)  # ending with 0
    printTest(242, True)  # palindrome with single middle
    printTest(2442, True)  # palindrome with double middle
    printTest(53745, False)  # non-palindrome
