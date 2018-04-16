#!/usr/bin/env python3
# https://leetcode.com/problems/container-with-most-water


class Solution(object):
    def maxArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # The intuition of the solution base on the following logic
        # ==========================================================
        # Statement: given current vertical lines chosen, any line that is
        #            shorter than the current vertical lines will never hold
        #            more water
        # Reason: width is shorter and height will not increase
        #
        # By above proposition,
        # - When current lines are different length, replace the shorter line
        # - When current lines are same, replace both

        start = 0
        end = len(heights) - 1
        currentMax = 0

        while start != -1 and end != -1:
            tmp = self.calculateHeight(heights, start, end)
            if tmp > currentMax:
                currentMax = tmp

            # select next candidate
            if heights[start] == heights[end]:
                start = self.findNext(heights, start, end)
                end = self.findNext(heights, end, start)
            elif heights[start] > heights[end]:
                end = self.findNext(heights, end, start)
            else:
                start = self.findNext(heights, start, end)

        return currentMax

    def findNext(self, heights, start, end):
        direction = 1
        if start > end:
            direction = -1

        for i in range(start, end, direction):
            if heights[i] > heights[start]:
                return i
        
        return -1

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

    # The test below are for testing the inward shifting logic
    printTest([5, 5, 1], 5)  # shift right
    printTest([1, 5, 5], 5)  # shift left
    printTest([1, 5, 5, 1], 5)  # shift both

