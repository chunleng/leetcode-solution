#!/usr/bin/env python2


class Solution(object):

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        # Number of character jump is based on
        jump = 2 * (numRows - 1)
        ans = ""

        for i in range(numRows):
            x = i
            while x < len(s):
                # Calculate the downstroke
                ans += s[x]

                # Calculate the diagonal
                if i != 0 and i != numRows - 1:
                    pos = x + 2 * (numRows - i - 1)
                    if pos < len(s):
                        ans += s[pos]

                x += jump

        return ans


def printTest(s, numRows, ans):
    out = Solution().convert(s, numRows)

    if ans == out:
        print("Test passed for {0}: output {1} == {2}".format(s, out, ans))
    else:
        print("Test failed for {0}: output {1} <> {2}".format(s, out, ans))


if __name__ == '__main__':
    # Base cases
    printTest("123", 1, "123")
    printTest("1", 2, "1")

    # Complete downstroke endings
    printTest("12345678", 2, "13572468")
    printTest("12345678901", 3, "15924680371")
    printTest("1234567890", 4, "1726835940")
    printTest("1234567890123", 5, "1928037146253")

    # Incomplete downstroke endings
    printTest("123456789", 3, "159246837")
