#!/usr/bin/env python3
# https://leetcode.com/problems/integer-to-roman/


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        num = 0
        current_index = 0

        while s[current_index:].startswith('M'):
            num += 1000
            current_index += 1

        if s[current_index:].startswith('CM'):
            num += 900
            current_index += 2

        if s[current_index:].startswith('D'):
            num += 500
            current_index += 1

        if s[current_index:].startswith('CD'):
            num += 400
            current_index += 2

        while s[current_index:].startswith('C'):
            num += 100
            current_index += 1

        if s[current_index:].startswith('XC'):
            num += 90
            current_index += 2

        if s[current_index:].startswith('L'):
            num += 50
            current_index += 1

        if s[current_index:].startswith('XL'):
            num += 40
            current_index += 2

        while s[current_index:].startswith('X'):
            num += 10
            current_index += 1

        if s[current_index:].startswith('IX'):
            num += 9
            current_index += 2

        if s[current_index:].startswith('V'):
            num += 5
            current_index += 1

        if s[current_index:].startswith('IV'):
            num += 4
            current_index += 2

        while s[current_index:].startswith('I'):
            num += 1
            current_index += 1

        return num


def printTest(s, ans):
    out = Solution().romanToInt(s)

    if ans == out:
        print("Test passed for %s: output - %s, expected - %s" % (s, out, ans))
    else:
        print("Test failed for %s: output - %s, expected - %s" % (s, out, ans))


if __name__ == '__main__':
    printTest('MMMCMXLVIII', 3948)  # cover most logical case
