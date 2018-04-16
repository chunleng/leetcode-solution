#!/usr/bin/env python3
# https://leetcode.com/problems/container-with-most-water


class Solution(object):
    def maxArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        currentMax = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                tmp = self.calculateHeight(heights, i, j)
                if tmp > currentMax:
                    currentMax = tmp

        return currentMax

    def calculateHeight(self, heights, x, y):
        """Get the container when i is x and y"""
        return min(heights[x], heights[y]) * abs(x-y)

def printTest(heights, ans):
    out = Solution().maxArea(heights)

    if ans == out:
        print("Test passed for %s: output - %s, expected - %s" % (heights, out, ans))
    else:
        print("Test failed for %s: output - %s, expected - %s" % (heights, out, ans))


if __name__ == '__main__':
    s = Solution()

    printTest([1, 1], 1)  # basic case
    printTest([1, 1, 1], 2)  # basic more than one across case
    printTest([1, 4, 4, 1], 4)  # bigger middle case
    printTest([4, 1, 1, 4], 12)  # bigger edge case

