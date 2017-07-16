#!/usr/bin/env python2
# https://leetcode.com/problems/string-to-integer-atoi

import re

INT_MAX = 2147483647
INT_MIN = -2147483648


class Solution(object):

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        # To demark whitespace trimming
        trimming = True
        positive_num = True
        ans = 0

        for c in str:
            if trimming:
                if re.match("\s", c):
                    continue
                else:
                    trimming = False
                    if c == "-":
                        positive_num = False
                        continue
                    elif c == "+":
                        continue

            num = self.lookupChar(c)

            if num is None:
                break

            ans = ans * 10 + self.lookupChar(c)

        # Python is kind of easier in this case as it does not have a max or min
        # integer
        return min(ans, INT_MAX) if positive_num else max(-ans, INT_MIN)

    def lookupChar(self, char):
        if char == "0":
            return 0
        elif char == "1":
            return 1
        elif char == "2":
            return 2
        elif char == "3":
            return 3
        elif char == "4":
            return 4
        elif char == "5":
            return 5
        elif char == "6":
            return 6
        elif char == "7":
            return 7
        elif char == "8":
            return 8
        elif char == "9":
            return 9

        return None


def printTest(x, ans):
    out = Solution().myAtoi(x)

    if ans == out:
        print("Test passed for {0}: output {1} == {2}".format(x, out, ans))
    else:
        print("Test failed for {0}: output {1} <> {2}".format(x, out, ans))

if __name__ == '__main__':
    s = Solution()

    printTest("1", 1)
    printTest(" 1", 1)
    printTest(" 	1", 1)
    printTest("-1", -1)
    printTest("a", 0)
    printTest("1a", 1)
    printTest("12a", 12)
    printTest("2147483647", 2147483647)
    printTest("-2147483648", -2147483648)
    printTest("2147483648", INT_MAX)
    printTest("-2147483649", INT_MIN)
    printTest(
        "-214748364811111111111111111111111111111111111111111111111111111111111111111111111111", INT_MIN)
    printTest(
        "-2147483648111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", INT_MIN)
