#!/usr/bin/env python3
# https://leetcode.com/problems/integer-to-roman/


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        roman = ''

        while num >= 1000:
            num -= 1000
            roman += 'M'

        if num >= 900:
            num -= 900
            roman += 'CM'

        if num >= 500:
            num -= 500
            roman += 'D'

        if num >= 400:
            num -= 400
            roman += 'CD'

        while num >= 100:
            num -= 100
            roman += 'C'

        if num >= 90:
            num -= 90
            roman += 'XC'

        if num >= 50:
            num -= 50
            roman += 'L'

        if num >= 40:
            num -= 40
            roman += 'XL'

        while num >= 10:
            num -= 10
            roman += 'X'

        if num >= 9:
            num -= 9
            roman += 'IX'

        if num >= 5:
            num -= 5
            roman += 'V'

        if num >= 4:
            num -= 4
            roman += 'IV'

        while num >= 1:
            num -= 1
            roman += 'I'

        return roman


def printTest(num, ans):
    out = Solution().intToRoman(num)

    if ans == out:
        print("Test passed for %s: output - %s, expected - %s" % (num, out, ans))
    else:
        print("Test failed for %s: output - %s, expected - %s" % (num, out, ans))


if __name__ == '__main__':
    printTest(3948, 'MMMCMXLVIII')  # cover most logical case
